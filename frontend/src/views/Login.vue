<template>
  <div class="login-container">
    <!-- 动态背景 -->
    <div class="login-background">
      <div class="floating-particles">
        <div class="particle" v-for="n in 15" :key="n" :style="getParticleStyle(n)"></div>
      </div>
      <div class="gradient-overlay"></div>
    </div>

    <!-- 主要内容 - 左右布局设计 -->
    <div class="login-content">
      <!-- 左侧品牌区域 -->
      <div class="login-left">
        <div class="brand-section">
          <!-- 品牌头部 -->
          <div class="brand-header">
            <div class="brand-logo">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M3 13h8V3H3v10zm0 8h8v-6H3v6zm10 0h8V11h-8v10zm0-18v6h8V3h-8z" fill="currentColor"/>
              </svg>
            </div>
            <div class="brand-info">
              <h1 class="brand-name">数据分析平台</h1>
              <p class="brand-tagline">智能 · 高效 · 专业</p>
            </div>
          </div>

          <!-- 欢迎信息 -->
          <div class="welcome-section">
            <h2 class="welcome-title">欢迎进入数据世界</h2>
            <p class="welcome-subtitle">专业的数据分析工具，让数据驱动您的决策</p>
          </div>

          <!-- 特性展示 -->
          <div class="features-showcase">
            <div class="feature-item" v-for="(feature, index) in features" :key="index">
              <div class="feature-icon" v-html="feature.icon"></div>
              <div class="feature-content">
                <h3 class="feature-title">{{ feature.title }}</h3>
                <p class="feature-description">{{ feature.description }}</p>
              </div>
            </div>
          </div>

          <!-- 统计数据 -->
          <div class="stats-section">
            <div class="stat-item" v-for="(stat, index) in stats" :key="index">
              <div class="stat-number">{{ stat.number }}</div>
              <div class="stat-label">{{ stat.label }}</div>
            </div>
          </div>
        </div>
      </div>

      <!-- 右侧登录区域 -->
      <div class="login-right">
        <div class="login-card glass-card">
          <!-- 登录头部 -->
          <div class="login-header">
            <h2 class="login-title">欢迎回来</h2>
            <p class="login-subtitle">请登录您的账户以继续使用平台服务</p>
          </div>

          <!-- 状态提示 -->
          <transition name="alert">
            <div v-if="loginStatus.show" :class="['login-alert', `alert-${loginStatus.type}`]">
              <div class="alert-icon">
                <svg v-if="loginStatus.type === 'success'" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <svg v-else-if="loginStatus.type === 'error'" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M12 9v3.75m9-.75a9 9 0 11-18 0 9 9 0 0118 0zm-9 3.75h.008v.008H12v-.008z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <svg v-else viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M11.25 11.25l.041-.02a.75.75 0 011.063.852l-.708 2.836a.75.75 0 001.063.853l.041-.021M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9-3.75h.008v.008H12V8.25z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
              <span class="alert-message">{{ loginStatus.message }}</span>
            </div>
          </transition>

          <!-- 演示账户信息 -->
          <div class="demo-info">
            <div class="demo-header">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 2L13.09 8.26L20 9L13.09 9.74L12 16L10.91 9.74L4 9L10.91 8.26L12 2Z" fill="currentColor"/>
              </svg>
              <span>演示账户</span>
            </div>
            <div class="demo-credentials">
              <div class="demo-item">
                <span class="demo-label">用户名</span>
                <code class="demo-value">admin</code>
              </div>
              <div class="demo-item">
                <span class="demo-label">密码</span>
                <code class="demo-value">admin123</code>
              </div>
            </div>
          </div>

          <!-- 登录表单 -->
          <form class="login-form" @submit.prevent="handleLogin">
            <div class="form-group">
              <label class="form-label">用户名</label>
              <div class="input-wrapper">
                <div class="input-icon">
                  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </div>
                <input
                  v-model="loginForm.username"
                  type="text"
                  class="form-input"
                  placeholder="请输入用户名"
                  @keyup.enter="handleLogin"
                  required
                />
              </div>
            </div>

            <div class="form-group">
              <label class="form-label">密码</label>
              <div class="input-wrapper">
                <div class="input-icon">
                  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </div>
                <input
                  v-model="loginForm.password"
                  :type="showPassword ? 'text' : 'password'"
                  class="form-input"
                  placeholder="请输入密码"
                  @keyup.enter="handleLogin"
                  required
                />
                <button
                  type="button"
                  class="password-toggle"
                  @click="togglePasswordVisibility"
                  tabindex="-1"
                >
                  <svg v-if="showPassword" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <svg v-else viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M3.98 8.223A10.477 10.477 0 001.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.45 10.45 0 0112 4.5c4.756 0 8.773 3.162 10.065 7.498a10.523 10.523 0 01-4.293 5.774M6.228 6.228L3 3m3.228 3.228l3.65 3.65m7.894 7.894L21 21m-3.228-3.228l-3.65-3.65m0 0a3 3 0 10-4.243-4.243m4.242 4.242L9.88 9.88" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </button>
              </div>
            </div>

            <div class="form-options">
              <label class="checkbox-wrapper">
                <input type="checkbox" v-model="loginForm.remember" class="checkbox-input">
                <span class="checkbox-custom"></span>
                <span class="checkbox-label">记住我</span>
              </label>
              <a href="#" class="forgot-link">忘记密码？</a>
            </div>

            <button
              type="submit"
              class="login-btn modern-btn"
              :disabled="loading"
            >
              <span v-if="loading" class="loading-spinner"></span>
              <span class="btn-text">{{ loading ? '登录中...' : '登录' }}</span>
              <div class="btn-shine"></div>
            </button>
          </form>

          <!-- 底部装饰 -->
          <div class="login-footer">
            <div class="feature-highlights">
              <div class="highlight-item">
                <div class="highlight-icon">
                  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </div>
                <span>安全可靠</span>
              </div>
              <div class="highlight-item">
                <div class="highlight-icon">
                  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M13 10V3L4 14h7v7l9-11h-7z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </div>
                <span>高效分析</span>
              </div>
              <div class="highlight-item">
                <div class="highlight-icon">
                  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </div>
                <span>专业服务</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '../store'

const router = useRouter()
const userStore = useUserStore()
const loading = ref(false)
const showPassword = ref(false)

// 登录状态提示
const loginStatus = reactive({
  show: false,
  type: 'info',
  message: '',
  icon: 'ℹ️'
})

// 登录表单
const loginForm = reactive({
  username: 'admin',
  password: 'admin123',
  remember: false
})

// 特性数据
const features = reactive([
  {
    icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M3 13h8V3H3v10zm0 8h8v-6H3v6zm10 0h8V11h-8v10zm0-18v6h8V3h-8z"/></svg>',
    title: '实时数据监控',
    description: '多维度数据实时展示与分析'
  },
  {
    icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>',
    title: '智能分析引擎',
    description: 'AI驱动的数据洞察与预测'
  },
  {
    icon: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M16 6l2.29 2.29-4.88 4.88-4-4L2 16.59 3.41 18l6-6 4 4 6.3-6.29L22 12V6z"/></svg>',
    title: '可视化报表',
    description: '丰富的图表展示与交互体验'
  }
])

// 统计数据
const stats = reactive([
  { number: '10K+', label: '活跃用户' },
  { number: '500+', label: '企业客户' },
  { number: '99.9%', label: '系统稳定性' }
])

// 检查是否已经登录
onMounted(() => {
  const token = localStorage.getItem('token')
  if (token) {
    loginStatus.show = true
    loginStatus.type = 'info'
    loginStatus.message = '您已经登录，即将跳转...'
    loginStatus.icon = 'ℹ️'

    setTimeout(() => {
      router.push('/')
    }, 1500)
  }
})

// 显示登录状态消息
const showStatusMessage = (type, message, icon) => {
  loginStatus.show = true
  loginStatus.type = type
  loginStatus.message = message
  loginStatus.icon = icon

  setTimeout(() => {
    loginStatus.show = false
  }, 3000)
}

// 处理登录
const handleLogin = async () => {
  // 简单验证
  if (!loginForm.username || !loginForm.password) {
    showStatusMessage('error', '请输入用户名和密码', '❌')
    return
  }

  // 移除表单验证，直接处理登录逻辑
  loading.value = true
  try {
    console.log('尝试登录...', loginForm)
    const user = await userStore.login(loginForm)

    // 确保登录状态正确设置
    if (user) {
      console.log('登录成功，用户状态已更新', user)

      // 立即强制刷新应用状态
      userStore.$patch({
        isAuthenticated: true,
        user: user
      })
    }

    showStatusMessage('success', '登录成功，即将跳转...', '✅')

    // 增加短暂停，确保状态有时间更新
    setTimeout(() => {
      router.push('/')
    }, 800)
  } catch (error) {
    console.error('登录失败:', error)
    showStatusMessage('error', '登录失败，请检查用户名和密码', '❌')
  } finally {
    loading.value = false
  }
}

// 切换密码可见性
const togglePasswordVisibility = () => {
  showPassword.value = !showPassword.value
}

// 生成粒子样式
const getParticleStyle = (index) => {
  const size = Math.random() * 4 + 2
  const left = Math.random() * 100
  const animationDelay = Math.random() * 20
  const animationDuration = Math.random() * 10 + 10

  return {
    width: `${size}px`,
    height: `${size}px`,
    left: `${left}%`,
    animationDelay: `${animationDelay}s`,
    animationDuration: `${animationDuration}s`
  }
}
</script>

<style scoped>
/* 登录容器 - 使用项目统一的深色主题 */
.login-container {
  height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  overflow: hidden;
  background: var(--bg-primary);
  color: var(--text-primary);
  font-family: var(--font-family);
}

/* 动态背景 */
.login-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
  overflow: hidden;
}

/* 浮动粒子 - 与项目主页保持一致 */
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

/* 主要内容 - 左右布局 */
.login-content {
  display: flex;
  width: 100%;
  height: 100%;
  max-width: 1200px;
  position: relative;
  z-index: 2;
}

/* 左侧品牌区域 */
.login-left {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-2xl);
  background: rgba(255, 255, 255, 0.02);
  backdrop-filter: blur(10px);
}

.brand-section {
  width: 100%;
  max-width: 500px;
  color: white;
  animation: slideInLeft 1s ease-out both;
}

/* 右侧登录区域 */
.login-right {
  flex: 0 0 420px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-2xl);
}

/* 登录卡片 - 右侧设计 */
.login-card {
  width: 100%;
  max-width: 380px;
  padding: var(--spacing-2xl);
  text-align: left;
  animation: slideInRight 1s ease-out 0.3s both;
}

/* 品牌头部 - 左侧布局设计 */
.brand-header {
  display: flex;
  align-items: center;
  gap: var(--spacing-lg);
  margin-bottom: var(--spacing-2xl);
}

.brand-logo {
  width: 64px;
  height: 64px;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  border-radius: var(--radius-lg);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: var(--shadow-glow);
  animation: pulse 2s infinite;
  flex-shrink: 0;
}

.brand-logo svg {
  width: 32px;
  height: 32px;
  color: white;
}

.brand-info {
  text-align: left;
}

.brand-name {
  font-size: 2.2rem;
  font-weight: 700;
  margin: 0;
  color: white;
  text-shadow: 0 2px 10px rgba(79, 172, 254, 0.3);
}

.brand-tagline {
  font-size: 1rem;
  margin: 0;
  color: rgba(255, 255, 255, 0.8);
  letter-spacing: 0.1em;
  font-weight: 400;
}

/* 欢迎区域 */
.welcome-section {
  margin-bottom: var(--spacing-2xl);
}

.welcome-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin: 0 0 var(--spacing-md) 0;
  color: white;
  line-height: 1.2;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
}

.welcome-subtitle {
  font-size: 1.1rem;
  margin: 0 0 var(--spacing-xl) 0;
  color: rgba(255, 255, 255, 0.9);
  line-height: 1.6;
}

/* 特性展示 */
.features-showcase {
  margin-bottom: var(--spacing-2xl);
}

.feature-item {
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
  margin-bottom: var(--spacing-lg);
  padding: var(--spacing-md);
  background: rgba(255, 255, 255, 0.1);
  border-radius: var(--radius-md);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  transition: var(--transition-normal);
}

.feature-item:hover {
  background: rgba(255, 255, 255, 0.15);
  transform: translateX(10px);
}

.feature-icon {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.feature-icon svg {
  width: 24px;
  height: 24px;
  color: white;
}

.feature-content {
  flex: 1;
}

.feature-title {
  font-size: 1.1rem;
  font-weight: 600;
  margin: 0 0 var(--spacing-xs) 0;
  color: white;
}

.feature-description {
  font-size: 0.9rem;
  margin: 0;
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.4;
}

/* 统计数据 */
.stats-section {
  display: flex;
  gap: var(--spacing-lg);
  margin-bottom: var(--spacing-xl);
}

.stat-item {
  flex: 1;
  text-align: center;
  padding: var(--spacing-lg);
  background: rgba(255, 255, 255, 0.1);
  border-radius: var(--radius-md);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.stat-number {
  font-size: 2rem;
  font-weight: 700;
  color: white;
  margin-bottom: var(--spacing-xs);
  text-shadow: 0 2px 10px rgba(79, 172, 254, 0.3);
}

.stat-label {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.8);
}

/* 登录头部 */
.login-header {
  text-align: center;
  margin-bottom: var(--spacing-xl);
}

.login-title {
  font-size: 1.8rem;
  font-weight: 700;
  color: var(--text-primary);
  margin: 0 0 var(--spacing-sm) 0;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.login-subtitle {
  font-size: 0.9rem;
  color: var(--text-secondary);
  margin: 0;
  line-height: 1.5;
}

/* 登录表单样式优化 */
.login-form {
  margin-bottom: var(--spacing-xl);
  text-align: left;
}

.form-group {
  margin-bottom: var(--spacing-lg);
}

.form-label {
  display: block;
  margin-bottom: var(--spacing-sm);
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text-primary);
}

.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.input-icon {
  position: absolute;
  left: var(--spacing-md);
  width: 20px;
  height: 20px;
  color: var(--text-muted);
  z-index: 2;
  transition: var(--transition-normal);
}

.form-input {
  width: 100%;
  height: 52px;
  padding: 0 var(--spacing-md) 0 3rem;
  background: var(--bg-glass);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  color: var(--text-primary);
  font-size: 1rem;
  transition: var(--transition-normal);
  font-family: inherit;
  backdrop-filter: blur(20px);
}

.form-input::placeholder {
  color: var(--text-muted);
  font-weight: 400;
}

.form-input:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(79, 172, 254, 0.1);
  background: rgba(255, 255, 255, 0.08);
}

.form-input:focus ~ .input-icon {
  color: var(--primary-color);
}

.password-toggle {
  position: absolute;
  right: var(--spacing-md);
  background: none;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  padding: var(--spacing-xs);
  border-radius: var(--radius-sm);
  transition: var(--transition-normal);
  z-index: 2;
}

.password-toggle:hover {
  color: var(--primary-color);
  background: rgba(79, 172, 254, 0.1);
}

.password-toggle svg {
  width: 18px;
  height: 18px;
}

/* 表单选项 */
.form-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--spacing-xl);
}

.checkbox-wrapper {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  cursor: pointer;
  font-size: 0.9rem;
  color: var(--text-secondary);
}

.checkbox-input {
  display: none;
}

.checkbox-custom {
  width: 18px;
  height: 18px;
  border: 2px solid var(--border-color);
  border-radius: var(--radius-sm);
  background: var(--bg-glass);
  position: relative;
  transition: var(--transition-normal);
}

.checkbox-input:checked + .checkbox-custom {
  background: var(--primary-color);
  border-color: var(--primary-color);
}

.checkbox-input:checked + .checkbox-custom::after {
  content: '✓';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-size: 12px;
  font-weight: bold;
}

.forgot-link {
  color: var(--primary-color);
  text-decoration: none;
  font-size: 0.9rem;
  transition: var(--transition-normal);
  position: relative;
}

.forgot-link:hover {
  color: var(--primary-dark);
}

.forgot-link::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
  transition: width 0.3s ease;
}

.forgot-link:hover::after {
  width: 100%;
}

/* 登录按钮 */
.login-btn {
  width: 100%;
  height: 52px;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  border: none;
  border-radius: var(--radius-md);
  color: white;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: var(--transition-normal);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: var(--spacing-sm);
  box-shadow: var(--shadow-md);
}

.login-btn:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg), var(--shadow-glow);
}

.login-btn:active {
  transform: translateY(0);
}

.login-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.loading-spinner {
  width: 18px;
  height: 18px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top: 2px solid white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
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

.login-btn:hover .btn-shine {
  left: 100%;
}

/* 状态提示 */
.login-alert {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  padding: var(--spacing-md);
  border-radius: var(--radius-md);
  margin-bottom: var(--spacing-lg);
  font-size: 0.9rem;
  font-weight: 500;
  backdrop-filter: blur(10px);
}

.alert-success {
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.3);
  color: var(--success-color);
}

.alert-error {
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.3);
  color: var(--error-color);
}

.alert-info {
  background: rgba(79, 172, 254, 0.1);
  border: 1px solid rgba(79, 172, 254, 0.3);
  color: var(--primary-color);
}

.alert-icon {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

.alert-enter-active, .alert-leave-active {
  transition: all 0.3s ease;
}

.alert-enter-from, .alert-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

/* 演示账户信息 */
.demo-info {
  background: rgba(79, 172, 254, 0.05);
  border: 1px solid rgba(79, 172, 254, 0.2);
  border-radius: var(--radius-md);
  padding: var(--spacing-md);
  margin-bottom: var(--spacing-lg);
}

.demo-header {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  margin-bottom: var(--spacing-sm);
  color: var(--primary-color);
  font-weight: 600;
  font-size: 0.9rem;
}

.demo-header svg {
  width: 16px;
  height: 16px;
}

.demo-credentials {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-xs);
}

.demo-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.85rem;
}

.demo-label {
  color: var(--text-secondary);
}

.demo-value {
  background: rgba(79, 172, 254, 0.1);
  color: var(--primary-color);
  padding: 2px 6px;
  border-radius: var(--radius-sm);
  font-family: 'Courier New', monospace;
  font-size: 0.8rem;
}

/* 底部装饰 */
.login-footer {
  border-top: 1px solid var(--border-color);
  padding-top: var(--spacing-lg);
  margin-top: var(--spacing-lg);
}

.feature-highlights {
  display: flex;
  justify-content: space-around;
  gap: var(--spacing-md);
}

.highlight-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--spacing-xs);
  font-size: 0.8rem;
  color: var(--text-muted);
  text-align: center;
}

.highlight-icon {
  width: 32px;
  height: 32px;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0.8;
}

.highlight-icon svg {
  width: 16px;
  height: 16px;
  color: white;
}

/* 动画效果 */
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

@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes slideInRight {
  from {
    opacity: 0;
    transform: translateX(50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes pulse {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
}

/* 玻璃态卡片样式 - 与项目保持一致 */
.glass-card {
  background: var(--bg-glass);
  backdrop-filter: blur(20px);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
  transition: var(--transition-normal);
}

.glass-card:hover {
  border-color: var(--border-hover);
  box-shadow: var(--shadow-glow);
}

/* 响应式设计 */
@media (max-width: 1024px) {
  .login-content {
    max-width: 900px;
  }

  .login-left {
    padding: var(--spacing-xl);
  }

  .login-right {
    flex: 0 0 380px;
    padding: var(--spacing-xl);
  }

  .welcome-title {
    font-size: 2.2rem;
  }

  .brand-name {
    font-size: 2rem;
  }
}

@media (max-width: 768px) {
  .login-content {
    flex-direction: column;
    padding: var(--spacing-lg);
  }

  .login-left {
    flex: none;
    padding: var(--spacing-lg) var(--spacing-md);
    text-align: center;
  }

  .login-right {
    flex: none;
    width: 100%;
    padding: var(--spacing-lg) var(--spacing-md);
  }

  .brand-header {
    justify-content: center;
    margin-bottom: var(--spacing-lg);
  }

  .brand-info {
    text-align: center;
  }

  .welcome-title {
    font-size: 1.8rem;
  }

  .brand-name {
    font-size: 1.6rem;
  }

  .features-showcase {
    display: none;
  }

  .stats-section {
    justify-content: center;
    gap: var(--spacing-md);
  }

  .stat-item {
    padding: var(--spacing-md);
  }

  .stat-number {
    font-size: 1.5rem;
  }
}

@media (max-width: 480px) {
  .login-container {
    padding: 0;
  }

  .login-left {
    padding: var(--spacing-md);
  }

  .login-right {
    padding: var(--spacing-md);
  }

  .login-card {
    padding: var(--spacing-lg);
  }

  .brand-name {
    font-size: 1.4rem;
  }

  .welcome-title {
    font-size: 1.5rem;
  }

  .login-title {
    font-size: 1.5rem;
  }

  .form-input {
    height: 48px;
  }

  .login-btn {
    height: 48px;
  }

  .stats-section {
    display: none;
  }
}

/* 确保在所有屏幕尺寸下都不出现滚动条 */
@media (max-height: 600px) {
  .login-left {
    padding: var(--spacing-md);
  }

  .login-right {
    padding: var(--spacing-md);
  }

  .welcome-section {
    margin-bottom: var(--spacing-lg);
  }

  .features-showcase {
    display: none;
  }

  .stats-section {
    display: none;
  }

  .login-card {
    padding: var(--spacing-lg);
  }

  .demo-info {
    margin-bottom: var(--spacing-md);
  }

  .form-group {
    margin-bottom: var(--spacing-md);
  }

  .form-options {
    margin-bottom: var(--spacing-md);
  }

  .login-footer {
    margin-top: var(--spacing-lg);
    padding-top: var(--spacing-lg);
  }

  .feature-highlights {
    gap: var(--spacing-md);
  }
}
</style>
