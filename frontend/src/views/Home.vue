<template>
  <div class="home-container">
    <!-- 顶部横幅区域 -->
    <div class="banner-section glass-card">
      <div class="banner-background">
        <div class="floating-particles">
          <div class="particle" v-for="i in 20" :key="i" :style="getParticleStyle(i)"></div>
        </div>
        <div class="gradient-overlay"></div>
      </div>

      <div class="banner-content">
        <div class="banner-icon">
          <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M3 13h8V3H3v10zm0 8h8v-6H3v6zm10 0h8V11h-8v10zm0-18v6h8V3h-8z" fill="currentColor"/>
          </svg>
        </div>
        <h1 class="banner-title">
          <span class="title-main">数据分析平台</span>
          <span class="title-subtitle">智能 · 高效 · 专业</span>
        </h1>
        <p class="banner-description">
          基于先进算法的企业级数据分析解决方案<br>
          让数据驱动您的每一个决策
        </p>
        <div class="banner-buttons">
          <button class="btn-primary modern-btn" @click="goToDashboard">
            <span class="btn-icon">🚀</span>
            <span class="btn-text">立即开始</span>
            <div class="btn-shine"></div>
          </button>
          <button class="btn-outline modern-btn" @click="showIntro = true">
            <span class="btn-icon">📖</span>
            <span class="btn-text">了解更多</span>
            <div class="btn-shine"></div>
          </button>
        </div>
        <div class="banner-stats">
          <div class="stat-item">
            <span class="stat-number">10K+</span>
            <span class="stat-label">企业用户</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">99.9%</span>
            <span class="stat-label">系统稳定性</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">24/7</span>
            <span class="stat-label">技术支持</span>
          </div>
        </div>
      </div>

      <div class="banner-visual">
        <div class="visual-element element-1">
          <div class="floating-icon">📊</div>
        </div>
        <div class="visual-element element-2">
          <div class="floating-icon">📈</div>
        </div>
        <div class="visual-element element-3">
          <div class="floating-icon">🎯</div>
        </div>
        <div class="data-flow">
          <div class="flow-line line-1"></div>
          <div class="flow-line line-2"></div>
          <div class="flow-line line-3"></div>
        </div>
      </div>
    </div>

    <!-- 功能卡片区域 -->
    <section class="features-section">
      <div class="section-header">
        <h2 class="section-title">
          <span class="title-icon">⭐</span>
          <span class="title-text">核心功能</span>
          <span class="title-decoration"></span>
        </h2>
        <p class="section-subtitle">强大的数据处理能力，满足您的各种分析需求</p>
      </div>

      <div class="feature-cards-grid">
        <div class="feature-card glass-card" @click="goToDashboard" data-aos="fade-up" data-aos-delay="100">
          <div class="card-header">
            <div class="card-icon dashboard-icon">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M3 13h8V3H3v10zm0 8h8v-6H3v6zm10 0h8V11h-8v10zm0-18v6h8V3h-8z" fill="currentColor"/>
              </svg>
            </div>
            <div class="card-badge">热门</div>
          </div>
          <div class="card-content">
            <h3 class="card-title">数据仪表盘</h3>
            <p class="card-description">实时监控关键业务指标，通过直观的图表和数据可视化，让您快速掌握业务全貌</p>
            <div class="card-features">
              <span class="feature-tag">实时数据</span>
              <span class="feature-tag">可视化</span>
              <span class="feature-tag">多维度</span>
            </div>
          </div>
          <div class="card-footer">
            <div class="card-action">
              <span class="action-text">查看仪表盘</span>
              <svg class="action-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
          </div>
          <div class="card-glow"></div>
        </div>

        <div class="feature-card glass-card" @click="goToAnalysis" data-aos="fade-up" data-aos-delay="200">
          <div class="card-header">
            <div class="card-icon analysis-icon">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.25 18L9 11.25l4.306 4.307a11.95 11.95 0 015.814-5.519l2.74-1.22m0 0l-5.94-2.28m5.94 2.28l-2.28 5.941" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <div class="card-badge">推荐</div>
          </div>
          <div class="card-content">
            <h3 class="card-title">数据分析</h3>
            <p class="card-description">运用先进的算法和机器学习技术，深度挖掘数据价值，发现业务增长机会</p>
            <div class="card-features">
              <span class="feature-tag">AI算法</span>
              <span class="feature-tag">趋势预测</span>
              <span class="feature-tag">智能洞察</span>
            </div>
          </div>
          <div class="card-footer">
            <div class="card-action">
              <span class="action-text">开始分析</span>
              <svg class="action-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
          </div>
          <div class="card-glow"></div>
        </div>

        <div class="feature-card glass-card" @click="goToReports" data-aos="fade-up" data-aos-delay="300">
          <div class="card-header">
            <div class="card-icon reports-icon">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <div class="card-badge">专业</div>
          </div>
          <div class="card-content">
            <h3 class="card-title">报表管理</h3>
            <p class="card-description">自动化生成专业级数据报表，支持多种格式导出，满足不同场景的汇报需求</p>
            <div class="card-features">
              <span class="feature-tag">自动生成</span>
              <span class="feature-tag">多格式</span>
              <span class="feature-tag">定制化</span>
            </div>
          </div>
          <div class="card-footer">
            <div class="card-action">
              <span class="action-text">管理报表</span>
              <svg class="action-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
          </div>
          <div class="card-glow"></div>
        </div>
      </div>
    </section>

    <!-- 平台优势区域 -->
    <section class="advantages-section">
      <div class="section-header">
        <h2 class="section-title">
          <span class="title-icon">💎</span>
          <span class="title-text">平台优势</span>
          <span class="title-decoration"></span>
        </h2>
        <p class="section-subtitle">领先的技术架构，为您提供卓越的数据分析体验</p>
      </div>

      <div class="advantages-grid">
        <div class="advantage-item glass-card" data-aos="zoom-in" data-aos-delay="100">
          <div class="advantage-icon">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <h4 class="advantage-title">多维数据分析</h4>
          <p class="advantage-description">从时间、空间、业务等多个维度深度挖掘数据价值</p>
          <div class="advantage-highlight">智能算法</div>
        </div>

        <div class="advantage-item glass-card" data-aos="zoom-in" data-aos-delay="200">
          <div class="advantage-icon">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M10.5 1.5H8.25A2.25 2.25 0 006 3.75v16.5a2.25 2.25 0 002.25 2.25h7.5A2.25 2.25 0 0018 20.25V3.75a2.25 2.25 0 00-2.25-2.25H13.5m-3 0V3h3V1.5m-3 0h3m-3 18.75h3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <h4 class="advantage-title">响应式设计</h4>
          <p class="advantage-description">完美适配桌面、平板、手机等各种设备屏幕</p>
          <div class="advantage-highlight">全端适配</div>
        </div>

        <div class="advantage-item glass-card" data-aos="zoom-in" data-aos-delay="300">
          <div class="advantage-icon">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <h4 class="advantage-title">企业级安全</h4>
          <p class="advantage-description">多层安全防护，确保您的数据资产绝对安全</p>
          <div class="advantage-highlight">银行级加密</div>
        </div>

        <div class="advantage-item glass-card" data-aos="zoom-in" data-aos-delay="400">
          <div class="advantage-icon">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <h4 class="advantage-title">极致性能</h4>
          <p class="advantage-description">分布式架构，毫秒级响应，轻松处理PB级数据</p>
          <div class="advantage-highlight">毫秒响应</div>
        </div>

        <div class="advantage-item glass-card" data-aos="zoom-in" data-aos-delay="500">
          <div class="advantage-icon">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <h4 class="advantage-title">实时同步</h4>
          <p class="advantage-description">数据变化实时反映，让您始终掌握最新动态</p>
          <div class="advantage-highlight">实时更新</div>
        </div>

        <div class="advantage-item glass-card" data-aos="zoom-in" data-aos-delay="600">
          <div class="advantage-icon">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 013 19.875v-6.75zM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V8.625zM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V4.125z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <h4 class="advantage-title">丰富图表</h4>
          <p class="advantage-description">50+种专业图表类型，满足各种数据展示需求</p>
          <div class="advantage-highlight">50+图表</div>
        </div>
      </div>
    </section>

    <!-- 成就数据区域 -->
    <section class="achievements-section glass-card">
      <div class="achievements-background">
        <div class="achievement-particles">
          <div class="achievement-particle" v-for="i in 15" :key="i" :style="getAchievementParticleStyle(i)"></div>
        </div>
      </div>

      <div class="section-header">
        <h2 class="section-title light">
          <span class="title-icon">🏆</span>
          <span class="title-text">平台成就</span>
        </h2>
        <p class="section-subtitle light">用数据说话，见证我们的专业实力</p>
      </div>

      <div class="achievements-grid">
        <div class="achievement-item" data-aos="fade-up" data-aos-delay="100">
          <div class="achievement-icon">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M20.25 6.375c0 2.278-3.694 4.125-8.25 4.125S3.75 8.653 3.75 6.375m16.5 0c0-2.278-3.694-4.125-8.25-4.125S3.75 4.097 3.75 6.375m16.5 0v11.25c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125V6.375m16.5 0v3.75m-16.5-3.75v3.75m16.5 0v3.75c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125v-3.75m16.5 0c0 2.278-3.694 4.125-8.25 4.125s-8.25-1.847-8.25-4.125" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <div class="achievement-number" ref="dataSourcesRef">{{ animatedDataSources }}</div>
          <div class="achievement-label">数据源接入</div>
          <div class="achievement-description">支持多种数据源类型</div>
        </div>

        <div class="achievement-item" data-aos="fade-up" data-aos-delay="200">
          <div class="achievement-icon">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M9.75 3.104v5.714a2.25 2.25 0 01-.659 1.591L5 14.5M9.75 3.104c-.251.023-.501.05-.75.082m.75-.082a24.301 24.301 0 014.5 0m0 0v5.714c0 .597.237 1.17.659 1.591L19.8 15.3M14.25 3.104c.251.023.501.05.75.082M19.8 15.3l-1.57.393A9.065 9.065 0 0112 15a9.065 9.065 0 00-6.23-.693L5 14.5m14.8.8l1.402 1.402c1.232 1.232.65 3.318-1.067 3.611A48.309 48.309 0 0112 21c-2.773 0-5.491-.235-8.135-.687-1.718-.293-2.3-2.379-1.067-3.611L5 14.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <div class="achievement-number" ref="modelsRef">{{ animatedModels }}</div>
          <div class="achievement-label">AI分析模型</div>
          <div class="achievement-description">覆盖各行业场景</div>
        </div>

        <div class="achievement-item" data-aos="fade-up" data-aos-delay="300">
          <div class="achievement-icon">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m2.25 0H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <div class="achievement-number" ref="reportsRef">{{ animatedReports }}</div>
          <div class="achievement-label">生成报表</div>
          <div class="achievement-description">累计服务报表数量</div>
        </div>

        <div class="achievement-item" data-aos="fade-up" data-aos-delay="400">
          <div class="achievement-icon">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M15.182 15.182a4.5 4.5 0 01-6.364 0M21 12a9 9 0 11-18 0 9 9 0 0118 0zM9.75 9.75c0 .414-.168.75-.375.75S9 10.164 9 9.75 9.168 9 9.375 9s.375.336.375.75zm-.375 0h.008v.015h-.008V9.75zm5.625 0c0 .414-.168.75-.375.75s-.375-.336-.375-.75.168-.75.375-.75.375.336.375.75zm-.375 0h.008v.015h-.008V9.75z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <div class="achievement-number" ref="satisfactionRef">{{ animatedSatisfaction }}%</div>
          <div class="achievement-label">客户满意度</div>
          <div class="achievement-description">持续优化用户体验</div>
        </div>
      </div>
    </section>

    <!-- 页脚区域 -->
    <footer class="modern-footer glass-card">
      <div class="footer-content">
        <div class="footer-brand">
          <div class="footer-logo">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M3 13h8V3H3v10zm0 8h8v-6H3v6zm10 0h8V11h-8v10zm0-18v6h8V3h-8z" fill="currentColor"/>
            </svg>
            <span class="footer-logo-text">数据分析平台</span>
          </div>
          <p class="footer-description">
            专业的企业级数据分析解决方案<br>
            让数据驱动您的每一个决策
          </p>
          <div class="footer-social">
            <a href="#" class="social-link" title="微信">
              <svg viewBox="0 0 24 24" fill="currentColor">
                <path d="M8.691 2.188C3.891 2.188 0 5.476 0 9.53c0 2.212 1.17 4.203 3.002 5.55a.59.59 0 0 1 .213.665l-.39 1.48c-.019.07-.048.141-.048.213 0 .163.13.295.29.295a.326.326 0 0 0 .167-.054l1.903-1.114a.864.864 0 0 1 .717-.098 10.16 10.16 0 0 0 2.837.403c.276 0 .543-.027.811-.05-.857-2.578.157-4.972 1.932-6.446 1.703-1.415 4.882-1.932 7.621-.55 1.545.781 2.765 2.205 3.429 4.006.4 1.082.24 2.246-.45 3.205-.12.168-.12.402 0 .57.12.168.336.168.456 0 .81-1.125 1.01-2.205.6-3.205-.69-1.68-2.205-3.205-4.006-4.006C14.691 2.188 11.691 2.188 8.691 2.188z"/>
              </svg>
            </a>
            <a href="#" class="social-link" title="微博">
              <svg viewBox="0 0 24 24" fill="currentColor">
                <path d="M9.31 16.242c-2.206 0-4.126-1.143-4.126-2.663 0-1.521 1.92-2.663 4.126-2.663s4.126 1.142 4.126 2.663c0 1.52-1.92 2.663-4.126 2.663zm8.74-4.126c-.413 0-.826-.275-.826-.688s.413-.688.826-.688.826.275.826.688-.413.688-.826.688zm-8.74-1.378c-1.378 0-2.481.826-2.481 1.929s1.103 1.929 2.481 1.929 2.481-.826 2.481-1.929-1.103-1.929-2.481-1.929z"/>
              </svg>
            </a>
            <a href="#" class="social-link" title="邮箱">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                <polyline points="22,6 12,13 2,6"/>
              </svg>
            </a>
          </div>
        </div>

        <div class="footer-links-section">
          <div class="footer-column">
            <h4 class="footer-column-title">产品功能</h4>
            <div class="footer-links">
              <a href="#" class="footer-link">数据仪表盘</a>
              <a href="#" class="footer-link">数据分析</a>
              <a href="#" class="footer-link">报表管理</a>
              <a href="#" class="footer-link">数字大屏</a>
            </div>
          </div>

          <div class="footer-column">
            <h4 class="footer-column-title">解决方案</h4>
            <div class="footer-links">
              <a href="#" class="footer-link">零售行业</a>
              <a href="#" class="footer-link">金融服务</a>
              <a href="#" class="footer-link">制造业</a>
              <a href="#" class="footer-link">教育行业</a>
            </div>
          </div>

          <div class="footer-column">
            <h4 class="footer-column-title">支持服务</h4>
            <div class="footer-links">
              <a href="#" class="footer-link">使用帮助</a>
              <a href="#" class="footer-link">API文档</a>
              <a href="#" class="footer-link">技术支持</a>
              <a href="#" class="footer-link">联系我们</a>
            </div>
          </div>

          <div class="footer-column">
            <h4 class="footer-column-title">关于我们</h4>
            <div class="footer-links">
              <a href="#" class="footer-link">公司介绍</a>
              <a href="#" class="footer-link">新闻动态</a>
              <a href="#" class="footer-link">招贤纳士</a>
              <a href="#" class="footer-link">隐私政策</a>
            </div>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <div class="footer-copyright">
          <p>© {{ currentYear }} 数据分析平台. 保留所有权利.</p>
          <p class="footer-icp">京ICP备12345678号-1</p>
        </div>
        <div class="footer-badges">
          <div class="security-badge">
            <span class="badge-icon">🔒</span>
            <span class="badge-text">SSL安全认证</span>
          </div>
          <div class="security-badge">
            <span class="badge-icon">✅</span>
            <span class="badge-text">ISO27001认证</span>
          </div>
        </div>
      </div>
    </footer>
    
    <!-- 介绍对话框 -->
    <div v-if="showIntro" class="modal">
      <div class="modal-content">
        <span class="close-btn" @click="showIntro = false">&times;</span>
        <h2>平台介绍</h2>
        <p>我们的数据分析平台提供了全面的数据处理、分析和可视化功能，帮助企业从海量数据中提取有价值的信息。</p>
        
        <h3>核心功能</h3>
        <ul>
          <li><strong>数据仪表盘：</strong> 实时监控业务关键指标</li>
          <li><strong>多维分析：</strong> 从多个角度探索数据规律</li>
          <li><strong>报表生成：</strong> 自动创建专业报表，支持多种格式导出</li>
          <li><strong>预测分析：</strong> 利用机器学习算法预测业务趋势</li>
        </ul>
        
        <div class="modal-footer">
          <button class="primary-btn" @click="goToDashboard">立即体验</button>
          <button class="outline-btn" @click="showIntro = false">关闭</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';

export default {
  name: 'HomeView',
  setup() {
    const router = useRouter();
    const showIntro = ref(false);

    // 数字动画相关
    const animatedDataSources = ref(0);
    const animatedModels = ref(0);
    const animatedReports = ref(0);
    const animatedSatisfaction = ref(0);

    const dataSourcesRef = ref(null);
    const modelsRef = ref(null);
    const reportsRef = ref(null);
    const satisfactionRef = ref(null);

    // 计算当前年份
    const currentYear = computed(() => new Date().getFullYear());

    // 粒子样式生成
    const getParticleStyle = (index) => {
      const size = Math.random() * 8 + 4;
      const left = Math.random() * 100;
      const animationDelay = Math.random() * 5;
      const animationDuration = Math.random() * 10 + 10;

      return {
        width: `${size}px`,
        height: `${size}px`,
        left: `${left}%`,
        animationDelay: `${animationDelay}s`,
        animationDuration: `${animationDuration}s`
      };
    };

    // 成就粒子样式生成
    const getAchievementParticleStyle = (index) => {
      const size = Math.random() * 6 + 3;
      const left = Math.random() * 100;
      const top = Math.random() * 100;
      const animationDelay = Math.random() * 3;
      const animationDuration = Math.random() * 8 + 8;

      return {
        width: `${size}px`,
        height: `${size}px`,
        left: `${left}%`,
        top: `${top}%`,
        animationDelay: `${animationDelay}s`,
        animationDuration: `${animationDuration}s`
      };
    };

    // 数字动画函数
    const animateNumber = (target, current, increment, callback) => {
      if (current < target) {
        callback(Math.min(current + increment, target));
        setTimeout(() => {
          animateNumber(target, current + increment, increment, callback);
        }, 50);
      }
    };

    // 启动数字动画
    const startNumberAnimations = () => {
      // 延迟启动动画，让页面先加载
      setTimeout(() => {
        animateNumber(100, 0, 2, (val) => animatedDataSources.value = val);
        animateNumber(50, 0, 1, (val) => animatedModels.value = val);
        animateNumber(1000, 0, 20, (val) => animatedReports.value = val);
        animateNumber(99, 0, 2, (val) => animatedSatisfaction.value = val);
      }, 1000);
    };

    // 路由导航函数
    const goToDashboard = () => {
      router.push('/dashboard');
    };

    const goToAnalysis = () => {
      router.push('/analysis');
    };

    const goToReports = () => {
      router.push('/reports');
    };

    // 组件挂载时启动动画
    onMounted(() => {
      startNumberAnimations();

      // 添加滚动动画观察器
      const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
      };

      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('animate-in');
          }
        });
      }, observerOptions);

      // 观察所有需要动画的元素
      document.querySelectorAll('.feature-card, .advantage-item, .achievement-item').forEach(el => {
        observer.observe(el);
      });
    });

    return {
      showIntro,
      currentYear,
      animatedDataSources,
      animatedModels,
      animatedReports,
      animatedSatisfaction,
      dataSourcesRef,
      modelsRef,
      reportsRef,
      satisfactionRef,
      getParticleStyle,
      getAchievementParticleStyle,
      goToDashboard,
      goToAnalysis,
      goToReports
    };
  }
};
</script>

<style scoped>
/* 基础样式 */
.home-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 var(--spacing-lg);
  font-family: var(--font-family);
  color: var(--text-primary);
  min-height: 100vh;
}

/* 玻璃态卡片基础样式 */
.glass-card {
  background: var(--bg-glass);
  backdrop-filter: blur(20px);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
  transition: var(--transition-normal);
}

/* 顶部横幅区域 */
.banner-section {
  position: relative;
  margin: var(--spacing-xl) 0;
  padding: var(--spacing-2xl) var(--spacing-xl);
  overflow: hidden;
  background: linear-gradient(135deg,
    rgba(79, 172, 254, 0.1) 0%,
    rgba(67, 233, 123, 0.1) 50%,
    rgba(240, 147, 251, 0.1) 100%);
  border: 1px solid rgba(79, 172, 254, 0.2);
  animation: fadeInUp 1s ease-out;
}

.banner-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
}

.floating-particles {
  position: absolute;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.particle {
  position: absolute;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  border-radius: 50%;
  opacity: 0.6;
  animation: floatParticle linear infinite;
}

@keyframes floatParticle {
  0% {
    transform: translateY(100vh) rotate(0deg);
    opacity: 0;
  }
  10% {
    opacity: 0.6;
  }
  90% {
    opacity: 0.6;
  }
  100% {
    transform: translateY(-100px) rotate(360deg);
    opacity: 0;
  }
}

.gradient-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg,
    rgba(79, 172, 254, 0.05) 0%,
    rgba(67, 233, 123, 0.05) 100%);
  z-index: 1;
}

/* 横幅内容区域 */
.banner-content {
  position: relative;
  z-index: 2;
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
}

.banner-icon {
  width: 80px;
  height: 80px;
  margin: 0 auto var(--spacing-lg);
  color: var(--primary-color);
  animation: pulse 2s infinite;
}

.banner-icon svg {
  width: 100%;
  height: 100%;
}

.banner-title {
  margin-bottom: var(--spacing-lg);
}

.title-main {
  display: block;
  font-size: 3.5rem;
  font-weight: 800;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: var(--spacing-sm);
  animation: slideInDown 1s ease-out 0.3s both;
}

.title-subtitle {
  display: block;
  font-size: 1.2rem;
  font-weight: 400;
  color: var(--text-secondary);
  letter-spacing: 0.2em;
  animation: slideInDown 1s ease-out 0.5s both;
}

.banner-description {
  font-size: 1.3rem;
  line-height: 1.6;
  color: var(--text-secondary);
  margin-bottom: var(--spacing-xl);
  animation: fadeIn 1s ease-out 0.7s both;
}

.banner-buttons {
  display: flex;
  gap: var(--spacing-lg);
  justify-content: center;
  margin-bottom: var(--spacing-xl);
  flex-wrap: wrap;
  animation: fadeInUp 1s ease-out 0.9s both;
}

/* 现代化按钮样式 */
.modern-btn {
  position: relative;
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  padding: var(--spacing-md) var(--spacing-xl);
  border: none;
  border-radius: var(--radius-md);
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition-normal);
  overflow: hidden;
  min-width: 160px;
  justify-content: center;
}

.btn-primary {
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  color: white;
  box-shadow: var(--shadow-md);
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-lg), var(--shadow-glow);
}

.btn-outline {
  background: transparent;
  color: var(--text-primary);
  border: 2px solid var(--border-hover);
}

.btn-outline:hover {
  background: rgba(79, 172, 254, 0.1);
  border-color: var(--primary-color);
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
}

.btn-icon {
  font-size: 1.2rem;
  transition: var(--transition-normal);
}

.modern-btn:hover .btn-icon {
  transform: scale(1.1);
}

.btn-shine {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: var(--transition-slow);
}

.modern-btn:hover .btn-shine {
  left: 100%;
}

/* 横幅统计数据 */
.banner-stats {
  display: flex;
  justify-content: center;
  gap: var(--spacing-xl);
  animation: fadeInUp 1s ease-out 1.1s both;
}

.banner-stats .stat-item {
  text-align: center;
  padding: var(--spacing-md);
  border-radius: var(--radius-md);
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: var(--transition-normal);
}

.banner-stats .stat-item:hover {
  transform: translateY(-2px);
  background: rgba(255, 255, 255, 0.08);
}

.banner-stats .stat-number {
  display: block;
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--primary-color);
  margin-bottom: var(--spacing-xs);
}

.banner-stats .stat-label {
  font-size: 0.9rem;
  color: var(--text-muted);
}

/* 横幅视觉元素 */
.banner-visual {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1;
  pointer-events: none;
}

.visual-element {
  position: absolute;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: linear-gradient(135deg,
    rgba(79, 172, 254, 0.2),
    rgba(67, 233, 123, 0.2));
  display: flex;
  align-items: center;
  justify-content: center;
  animation: float 6s ease-in-out infinite;
}

.element-1 {
  top: 20%;
  right: 10%;
  animation-delay: 0s;
}

.element-2 {
  bottom: 30%;
  left: 5%;
  animation-delay: 2s;
}

.element-3 {
  top: 60%;
  right: 20%;
  animation-delay: 4s;
}

.floating-icon {
  font-size: 1.5rem;
  animation: pulse 2s infinite;
}

.data-flow {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.flow-line {
  position: absolute;
  height: 2px;
  background: linear-gradient(90deg,
    transparent,
    var(--primary-color),
    transparent);
  animation: flowLine 4s linear infinite;
}

.line-1 {
  top: 25%;
  left: 10%;
  right: 10%;
  animation-delay: 0s;
}

.line-2 {
  top: 50%;
  left: 15%;
  right: 15%;
  animation-delay: 1.5s;
}

.line-3 {
  top: 75%;
  left: 20%;
  right: 20%;
  animation-delay: 3s;
}

@keyframes flowLine {
  0% {
    transform: translateX(-100%);
    opacity: 0;
  }
  50% {
    opacity: 1;
  }
  100% {
    transform: translateX(100%);
    opacity: 0;
  }
}

/* 通用动画 */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideInDown {
  from {
    opacity: 0;
    transform: translateY(-30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

@keyframes float {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(180deg); }
}

/* 章节样式 */
.features-section,
.advantages-section,
.achievements-section {
  margin: var(--spacing-2xl) 0;
}

.section-header {
  text-align: center;
  margin-bottom: var(--spacing-2xl);
}

.section-title {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: var(--spacing-md);
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: var(--spacing-md);
  position: relative;
}

.section-title.light {
  color: var(--text-primary);
}

.title-icon {
  font-size: 2rem;
  animation: pulse 2s infinite;
}

.title-text {
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.title-decoration {
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 4px;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  border-radius: 2px;
}

.section-subtitle {
  font-size: 1.2rem;
  color: var(--text-secondary);
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.6;
}

.section-subtitle.light {
  color: var(--text-secondary);
}

/* 功能卡片网格 */
.feature-cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: var(--spacing-xl);
  margin-bottom: var(--spacing-2xl);
}

.feature-card {
  position: relative;
  padding: var(--spacing-xl);
  cursor: pointer;
  transition: var(--transition-normal);
  overflow: hidden;
  border: 1px solid rgba(79, 172, 254, 0.1);
}

.feature-card:hover {
  transform: translateY(-8px);
  border-color: rgba(79, 172, 254, 0.3);
  box-shadow: var(--shadow-lg), 0 0 30px rgba(79, 172, 254, 0.2);
}

.feature-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  transform: scaleX(0);
  transition: var(--transition-normal);
}

.feature-card:hover::before {
  transform: scaleX(1);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: var(--spacing-lg);
}

.card-badge {
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  color: white;
  padding: var(--spacing-xs) var(--spacing-sm);
  border-radius: var(--radius-sm);
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.card-glow {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg,
    rgba(79, 172, 254, 0.05),
    rgba(67, 233, 123, 0.05));
  opacity: 0;
  transition: var(--transition-normal);
  pointer-events: none;
}

.feature-card:hover .card-glow {
  opacity: 1;
}

/* 卡片图标 */
.card-icon {
  width: 80px;
  height: 80px;
  border-radius: var(--radius-lg);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  transition: var(--transition-normal);
}

.card-icon svg {
  width: 40px;
  height: 40px;
  transition: var(--transition-normal);
}

.dashboard-icon {
  background: linear-gradient(135deg,
    rgba(79, 172, 254, 0.1),
    rgba(79, 172, 254, 0.2));
  color: var(--primary-color);
}

.analysis-icon {
  background: linear-gradient(135deg,
    rgba(67, 233, 123, 0.1),
    rgba(67, 233, 123, 0.2));
  color: var(--secondary-color);
}

.reports-icon {
  background: linear-gradient(135deg,
    rgba(240, 147, 251, 0.1),
    rgba(240, 147, 251, 0.2));
  color: var(--accent-color);
}

.feature-card:hover .card-icon {
  transform: scale(1.1) rotate(5deg);
}

.feature-card:hover .card-icon svg {
  transform: scale(1.1);
}

/* 卡片内容 */
.card-content {
  margin-bottom: var(--spacing-lg);
}

.card-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: var(--spacing-md);
}

.card-description {
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: var(--spacing-md);
  font-size: 1rem;
}

.card-features {
  display: flex;
  gap: var(--spacing-sm);
  flex-wrap: wrap;
}

.feature-tag {
  background: rgba(79, 172, 254, 0.1);
  color: var(--primary-color);
  padding: var(--spacing-xs) var(--spacing-sm);
  border-radius: var(--radius-sm);
  font-size: 0.8rem;
  font-weight: 500;
  border: 1px solid rgba(79, 172, 254, 0.2);
}

/* 卡片底部 */
.card-footer {
  border-top: 1px solid var(--border-color);
  padding-top: var(--spacing-md);
}

.card-action {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  color: var(--primary-color);
  font-weight: 600;
  transition: var(--transition-normal);
}

.action-icon {
  width: 16px;
  height: 16px;
  transition: var(--transition-normal);
}

.feature-card:hover .card-action {
  color: var(--secondary-color);
}

.feature-card:hover .action-icon {
  transform: translateX(4px);
}

/* 优势网格 */
.advantages-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: var(--spacing-xl);
  margin-bottom: var(--spacing-2xl);
}

.advantage-item {
  padding: var(--spacing-xl);
  text-align: center;
  transition: var(--transition-normal);
  position: relative;
  overflow: hidden;
  border: 1px solid rgba(79, 172, 254, 0.1);
}

.advantage-item:hover {
  transform: translateY(-5px);
  border-color: rgba(79, 172, 254, 0.3);
  box-shadow: var(--shadow-lg), 0 0 25px rgba(79, 172, 254, 0.15);
}

.advantage-item::before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 3px;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  transition: var(--transition-normal);
}

.advantage-item:hover::before {
  width: 100%;
}

.advantage-icon {
  width: 80px;
  height: 80px;
  margin: 0 auto var(--spacing-lg);
  border-radius: 50%;
  background: linear-gradient(135deg,
    rgba(79, 172, 254, 0.1),
    rgba(67, 233, 123, 0.1));
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--primary-color);
  transition: var(--transition-normal);
}

.advantage-icon svg {
  width: 32px;
  height: 32px;
}

.advantage-item:hover .advantage-icon {
  transform: scale(1.1);
  background: linear-gradient(135deg,
    rgba(79, 172, 254, 0.2),
    rgba(67, 233, 123, 0.2));
}

.advantage-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: var(--spacing-md);
}

.advantage-description {
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: var(--spacing-md);
}

.advantage-highlight {
  display: inline-block;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  color: white;
  padding: var(--spacing-xs) var(--spacing-md);
  border-radius: var(--radius-sm);
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* 成就数据区域 */
.achievements-section {
  position: relative;
  padding: var(--spacing-2xl);
  margin: var(--spacing-2xl) 0;
  background: linear-gradient(135deg,
    rgba(79, 172, 254, 0.1) 0%,
    rgba(67, 233, 123, 0.1) 50%,
    rgba(240, 147, 251, 0.1) 100%);
  border: 1px solid rgba(79, 172, 254, 0.2);
  overflow: hidden;
}

.achievements-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
}

.achievement-particles {
  position: absolute;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.achievement-particle {
  position: absolute;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  border-radius: 50%;
  opacity: 0.3;
  animation: floatAchievement linear infinite;
}

@keyframes floatAchievement {
  0% {
    transform: translateY(0) rotate(0deg);
    opacity: 0.3;
  }
  50% {
    opacity: 0.6;
  }
  100% {
    transform: translateY(-20px) rotate(360deg);
    opacity: 0.3;
  }
}

.achievements-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: var(--spacing-xl);
  position: relative;
  z-index: 1;
}

.achievement-item {
  text-align: center;
  padding: var(--spacing-xl);
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: var(--radius-lg);
  transition: var(--transition-normal);
}

.achievement-item:hover {
  transform: translateY(-5px);
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(79, 172, 254, 0.3);
  box-shadow: var(--shadow-lg);
}

.achievement-icon {
  width: 60px;
  height: 60px;
  margin: 0 auto var(--spacing-md);
  border-radius: 50%;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  transition: var(--transition-normal);
}

.achievement-icon svg {
  width: 24px;
  height: 24px;
}

.achievement-item:hover .achievement-icon {
  transform: scale(1.1) rotate(5deg);
}

.achievement-number {
  font-size: 3rem;
  font-weight: 800;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: var(--spacing-sm);
  line-height: 1;
}

.achievement-label {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: var(--spacing-xs);
}

.achievement-description {
  font-size: 0.9rem;
  color: var(--text-muted);
}

/* 现代化页脚 */
.modern-footer {
  margin: var(--spacing-2xl) 0 var(--spacing-lg);
  padding: var(--spacing-2xl);
  border: 1px solid rgba(79, 172, 254, 0.1);
}

.footer-content {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: var(--spacing-2xl);
  margin-bottom: var(--spacing-xl);
}

.footer-brand {
  max-width: 400px;
}

.footer-logo {
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
  margin-bottom: var(--spacing-lg);
}

.footer-logo svg {
  width: 32px;
  height: 32px;
  color: var(--primary-color);
}

.footer-logo-text {
  font-size: 1.5rem;
  font-weight: 700;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.footer-description {
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: var(--spacing-lg);
}

.footer-social {
  display: flex;
  gap: var(--spacing-md);
}

.social-link {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(79, 172, 254, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--primary-color);
  transition: var(--transition-normal);
}

.social-link:hover {
  background: var(--primary-color);
  color: white;
  transform: translateY(-2px);
}

.social-link svg {
  width: 18px;
  height: 18px;
}

.footer-links-section {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: var(--spacing-xl);
}

.footer-column-title {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: var(--spacing-md);
}

.footer-links {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-sm);
}

.footer-link {
  color: var(--text-secondary);
  text-decoration: none;
  transition: var(--transition-normal);
  padding: var(--spacing-xs) 0;
}

.footer-link:hover {
  color: var(--primary-color);
  padding-left: var(--spacing-sm);
}

.footer-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: var(--spacing-lg);
  border-top: 1px solid var(--border-color);
}

.footer-copyright {
  color: var(--text-muted);
}

.footer-icp {
  font-size: 0.9rem;
  margin-top: var(--spacing-xs);
}

.footer-badges {
  display: flex;
  gap: var(--spacing-md);
}

.security-badge {
  display: flex;
  align-items: center;
  gap: var(--spacing-xs);
  padding: var(--spacing-xs) var(--spacing-sm);
  background: rgba(79, 172, 254, 0.1);
  border-radius: var(--radius-sm);
  font-size: 0.8rem;
  color: var(--primary-color);
}

.badge-icon {
  font-size: 0.9rem;
}

/* 介绍对话框 */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(5px);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  animation: fadeIn 0.3s ease-out;
}

.modal-content {
  background: var(--bg-glass);
  backdrop-filter: blur(20px);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: var(--spacing-2xl);
  max-width: 600px;
  width: 90%;
  max-height: 80vh;
  overflow-y: auto;
  position: relative;
  box-shadow: var(--shadow-lg);
  color: var(--text-primary);
  animation: scaleIn 0.3s ease-out;
}

@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.close-btn {
  position: absolute;
  top: var(--spacing-lg);
  right: var(--spacing-lg);
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  cursor: pointer;
  color: var(--text-secondary);
  transition: var(--transition-normal);
}

.close-btn:hover {
  background: rgba(255, 255, 255, 0.2);
  color: var(--text-primary);
}

.modal-content h2 {
  margin-bottom: var(--spacing-lg);
  color: var(--primary-color);
  font-size: 1.8rem;
}

.modal-content h3 {
  margin: var(--spacing-lg) 0 var(--spacing-md);
  color: var(--text-primary);
}

.modal-content p,
.modal-content li {
  line-height: 1.6;
  color: var(--text-secondary);
}

.modal-content ul {
  padding-left: var(--spacing-lg);
  margin-bottom: var(--spacing-lg);
}

.modal-content li {
  margin-bottom: var(--spacing-sm);
}

.modal-footer {
  margin-top: var(--spacing-xl);
  display: flex;
  justify-content: flex-end;
  gap: var(--spacing-md);
}

/* 响应式设计 */
@media (max-width: 1024px) {
  .home-container {
    padding: 0 var(--spacing-md);
  }

  .banner-section {
    padding: var(--spacing-xl) var(--spacing-lg);
  }

  .title-main {
    font-size: 3rem;
  }

  .feature-cards-grid {
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  }

  .advantages-grid {
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  }

  .footer-content {
    grid-template-columns: 1fr;
    gap: var(--spacing-xl);
  }

  .footer-links-section {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .banner-section {
    padding: var(--spacing-lg);
    margin: var(--spacing-lg) 0;
  }

  .title-main {
    font-size: 2.5rem;
  }

  .banner-description {
    font-size: 1.1rem;
  }

  .banner-buttons {
    flex-direction: column;
    align-items: center;
  }

  .modern-btn {
    width: 100%;
    max-width: 280px;
  }

  .banner-stats {
    flex-direction: column;
    gap: var(--spacing-md);
  }

  .feature-cards-grid {
    grid-template-columns: 1fr;
    gap: var(--spacing-lg);
  }

  .advantages-grid {
    grid-template-columns: 1fr;
    gap: var(--spacing-lg);
  }

  .achievements-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: var(--spacing-lg);
  }

  .footer-links-section {
    grid-template-columns: 1fr;
    gap: var(--spacing-lg);
  }

  .footer-bottom {
    flex-direction: column;
    gap: var(--spacing-md);
    text-align: center;
  }

  .visual-element {
    display: none;
  }

  .data-flow {
    display: none;
  }
}

@media (max-width: 480px) {
  .title-main {
    font-size: 2rem;
  }

  .section-title {
    font-size: 2rem;
  }

  .achievements-grid {
    grid-template-columns: 1fr;
  }

  .achievement-number {
    font-size: 2.5rem;
  }

  .footer-badges {
    flex-direction: column;
    align-items: center;
  }
}

/* 滚动动画 */
.animate-in {
  animation: fadeInUp 0.6s ease-out;
}

/* 浅色主题下的首页样式优化 */
.light-theme .title-main {
  background: linear-gradient(135deg, #1e40af, #7c3aed) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  background-clip: text !important;
  font-weight: 900 !important;
}

.light-theme .title-subtitle {
  color: #000000 !important;
  font-weight: 700 !important;
  text-shadow: none !important;
}

.light-theme .banner-description {
  color: #1a202c !important;
  font-weight: 600 !important;
  text-shadow: none !important;
}

.light-theme .section-title {
  color: #000000 !important;
  font-weight: 800 !important;
  text-shadow: none !important;
}

.light-theme .title-text {
  background: linear-gradient(135deg, #1e40af, #7c3aed) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  background-clip: text !important;
}

.light-theme .section-subtitle {
  color: #1a202c !important;
  font-weight: 600 !important;
  text-shadow: none !important;
}

.light-theme .card-title {
  color: #000000 !important;
  font-weight: 800 !important;
  text-shadow: none !important;
}

.light-theme .card-description {
  color: #1a202c !important;
  font-weight: 500 !important;
  text-shadow: none !important;
}

.light-theme .stat-number {
  color: #1e40af !important;
  font-weight: 800 !important;
}

.light-theme .stat-label {
  color: #2d3748 !important;
  font-weight: 600 !important;
}

.light-theme .advantage-title {
  color: #000000 !important;
  font-weight: 800 !important;
  text-shadow: none !important;
}

.light-theme .advantage-description {
  color: #1a202c !important;
  font-weight: 500 !important;
  text-shadow: none !important;
}

.light-theme .achievement-number {
  color: #1e40af !important;
  font-weight: 900 !important;
}

.light-theme .achievement-label {
  color: #000000 !important;
  font-weight: 700 !important;
}

.light-theme .footer-title {
  color: #000000 !important;
  font-weight: 800 !important;
}

.light-theme .footer-link {
  color: #1a202c !important;
  font-weight: 500 !important;
}

.light-theme .footer-link:hover {
  color: #1e40af !important;
}

.light-theme .modal-content h2,
.light-theme .modal-content h3 {
  color: #000000 !important;
  font-weight: 800 !important;
}

.light-theme .modal-content p,
.light-theme .modal-content li {
  color: #1a202c !important;
  font-weight: 500 !important;
}

/* 性能优化 */
.feature-card,
.advantage-item,
.achievement-item {
  will-change: transform;
}

.particle,
.achievement-particle {
  will-change: transform, opacity;
}
</style>