<template>
  <div class="app-container">
    <!-- 现代化导航栏 - 仅在登录状态下显示 -->
    <nav class="main-nav glass-card" v-if="isLoggedIn">
      <div class="nav-container">
        <!-- Logo区域 -->
        <div class="nav-logo">
          <router-link to="/" class="logo-link">
            <div class="logo-icon">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M3 13h8V3H3v10zm0 8h8v-6H3v6zm10 0h8V11h-8v10zm0-18v6h8V3h-8z" fill="currentColor"/>
              </svg>
            </div>
            <span class="logo-text">{{ t('common.appName') || '数据分析平台' }}</span>
          </router-link>
        </div>

        <!-- 导航链接 -->
        <div class="nav-links">
          <router-link to="/" exact-active-class="active" class="nav-link">
            <span class="link-icon">🏠</span>
            <span class="link-text">{{ t('nav.home') || '首页' }}</span>
          </router-link>
          <router-link to="/dashboard" active-class="active" class="nav-link">
            <span class="link-icon">📊</span>
            <span class="link-text">{{ t('nav.dashboard') || '数据仪表盘' }}</span>
          </router-link>
          <router-link to="/analysis" active-class="active" class="nav-link">
            <span class="link-icon">📈</span>
            <span class="link-text">{{ t('nav.analysis') || '数据分析' }}</span>
          </router-link>
          <router-link to="/reports" active-class="active" class="nav-link">
            <span class="link-icon">📋</span>
            <span class="link-text">{{ t('nav.reports') || '报表管理' }}</span>
          </router-link>
          <router-link to="/datascreen" active-class="active" class="nav-link">
            <span class="link-icon">🖥️</span>
            <span class="link-text">{{ t('nav.dataScreen') || '数字大屏' }}</span>
          </router-link>
        </div>

        <!-- 右侧操作区 -->
        <div class="nav-actions">
          <!-- 全局搜索组件 -->
          <GlobalSearch ref="globalSearch" />

          <!-- 通知中心组件 -->
          <NotificationCenter />

          <div class="user-section">
            <button class="user-btn" @click="toggleUserMenu" title="用户菜单">
              <div class="user-avatar">
                <span>{{ (userStore.getUser?.username || 'U').charAt(0).toUpperCase() }}</span>
              </div>
              <div class="user-info-inline">
                <span class="user-name">{{ userStore.getUser?.username || t('user.defaultName') || '用户' }}</span>
                <span class="user-role">{{ userStore.getUser?.role === 'admin' ? (t('user.role.admin') || '管理员') : (t('user.role.user') || '普通用户') }}</span>
              </div>
              <svg class="dropdown-icon" :class="{ 'rotated': showUserMenu }" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="m19.5 8.25-7.5 7.5-7.5-7.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>

            <!-- 用户下拉菜单 -->
            <transition name="dropdown">
              <div class="user-menu glass-card" v-if="showUserMenu">
                <div class="menu-header">
                  <div class="user-avatar-large">
                    <span>{{ (userStore.getUser?.username || 'U').charAt(0).toUpperCase() }}</span>
                  </div>
                  <div class="user-details">
                    <div class="user-name">{{ userStore.getUser?.username || t('user.defaultName') || '用户' }}</div>
                    <div class="user-email">user@example.com</div>
                    <div class="user-role badge badge-primary">{{ userStore.getUser?.role === 'admin' ? (t('user.role.admin') || '管理员') : (t('user.role.user') || '普通用户') }}</div>
                  </div>
                </div>

                <div class="menu-divider"></div>

                <div class="menu-items">
                  <router-link to="/profile" class="menu-item" @click="closeUserMenu">
                    <svg class="menu-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <span>{{ t('user.profile') || '个人资料' }}</span>
                  </router-link>

                  <router-link to="/settings" class="menu-item" @click="closeUserMenu">
                    <svg class="menu-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M9.594 3.94c.09-.542.56-.94 1.11-.94h2.593c.55 0 1.02.398 1.11.94l.213 1.281c.063.374.313.686.645.87.074.04.147.083.22.127.325.196.72.257 1.075.124l1.217-.456a1.125 1.125 0 0 1 1.37.49l1.296 2.247a1.125 1.125 0 0 1-.26 1.431l-1.003.827c-.293.241-.438.613-.43.992a6.759 6.759 0 0 1 0 .255c-.008.378.137.75.43.991l1.004.827c.424.35.534.955.26 1.43l-1.298 2.247a1.125 1.125 0 0 1-1.369.491l-1.217-.456c-.355-.133-.75-.072-1.076.124a6.57 6.57 0 0 1-.22.128c-.331.183-.581.495-.644.869l-.213 1.281c-.09.543-.56.94-1.11.94h-2.594c-.55 0-1.019-.398-1.11-.94l-.213-1.281c-.062-.374-.312-.686-.644-.87a6.52 6.52 0 0 1-.22-.127c-.325-.196-.72-.257-1.076-.124l-1.217.456a1.125 1.125 0 0 1-1.369-.49l-1.297-2.247a1.125 1.125 0 0 1 .26-1.431l1.004-.827c.292-.24.437-.613.43-.991a6.932 6.932 0 0 1 0-.255c.007-.38-.138-.751-.43-.992l-1.004-.827a1.125 1.125 0 0 1-.26-1.43l1.297-2.247a1.125 1.125 0 0 1 1.37-.491l1.216.456c.356.133.751.072 1.076-.124.072-.044.146-.086.22-.128.332-.183.582-.495.644-.869l.214-1.28Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                      <path d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <span>{{ t('user.settings') || '设置' }}</span>
                  </router-link>

                  <div class="menu-divider"></div>

                  <div class="menu-item logout-item" @click="logout">
                    <svg class="menu-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M15.75 9V5.25A2.25 2.25 0 0 0 13.5 3h-6a2.25 2.25 0 0 0-2.25 2.25v13.5A2.25 2.25 0 0 0 7.5 21h6a2.25 2.25 0 0 0 2.25-2.25V15M12 9l-3 3m0 0 3 3m-3-3h12.75" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <span>{{ t('user.logout') || '退出登录' }}</span>
                  </div>
                </div>
              </div>
            </transition>
          </div>
        </div>
      </div>
    </nav>

    <!-- 主要内容区域 -->
    <main class="main-content">
      <router-view/>
    </main>

    <!-- 背景装饰 -->
    <div class="bg-decoration">
      <div class="decoration-circle circle-1"></div>
      <div class="decoration-circle circle-2"></div>
      <div class="decoration-circle circle-3"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, watch } from 'vue'
import { useI18n } from 'vue-i18n'
import { useUserStore, useSettingsStore } from './store'
import { useRouter } from 'vue-router'
import GlobalSearch from './components/GlobalSearch.vue'
import NotificationCenter from './components/NotificationCenter.vue'

const { t } = useI18n()

const userStore = useUserStore()
const settingsStore = useSettingsStore()
const router = useRouter()
const showUserMenu = ref(false)
const globalSearch = ref(null)

// 计算是否已登录
const isLoggedIn = ref(false)

// 监听身份验证状态
onMounted(async () => {
  checkAuthStatus()

  // 延迟一点确保DOM完全准备好
  await new Promise(resolve => setTimeout(resolve, 100))

  // 初始化设置
  try {
    await settingsStore.loadSettings()
    console.log('设置初始化完成')
  } catch (error) {
    console.error('设置初始化失败:', error)
  }
})

// 监听用户存储的身份验证状态变化
watch(
  () => userStore.isLoggedIn,
  (newValue) => {
    isLoggedIn.value = newValue
    console.log('登录状态已更新:', newValue)
  }
)

// 监听路由变化，确保身份验证状态是最新的
watch(
  () => router.currentRoute.value,
  () => {
    checkAuthStatus()
  }
)

// 监听主题变化
watch(
  () => settingsStore.theme,
  (newTheme) => {
    console.log('主题变化监听器触发:', newTheme)
    settingsStore.applyTheme()
  }
)

// 监听语言变化
watch(
  () => settingsStore.language,
  (newLanguage) => {
    console.log('语言变化监听器触发:', newLanguage)
    settingsStore.applyLanguage(newLanguage)
    // 延迟调整导航栏布局，确保语言已切换
    setTimeout(() => {
      adjustNavLayout()
    }, 100)
  }
)

function checkAuthStatus() {
  isLoggedIn.value = userStore.isLoggedIn || !!localStorage.getItem('token')
  console.log('检查登录状态:', isLoggedIn.value)
}

// 切换用户菜单显示
function toggleUserMenu() {
  showUserMenu.value = !showUserMenu.value
}

// 关闭用户菜单
function closeUserMenu() {
  showUserMenu.value = false
}

// 点击页面其他地方关闭用户菜单
function closeMenuOnOutsideClick(event) {
  const userBtn = document.querySelector('.user-btn')
  const userMenu = document.querySelector('.user-menu')
  
  if (userBtn && userMenu && showUserMenu.value) {
    if (!userBtn.contains(event.target) && !userMenu.contains(event.target)) {
      showUserMenu.value = false
    }
  }
}

// 退出登录
function logout() {
  userStore.logout()
  router.push('/login')
  showUserMenu.value = false
}

// 调整导航栏布局
function adjustNavLayout() {
  const navLinks = document.querySelector('.nav-links')
  const navContainer = document.querySelector('.nav-container')

  if (!navLinks || !navContainer) return

  // 检查导航链接是否溢出
  const containerWidth = navContainer.offsetWidth
  const logoWidth = document.querySelector('.nav-logo')?.offsetWidth || 0
  const actionsWidth = document.querySelector('.nav-actions')?.offsetWidth || 0
  const availableWidth = containerWidth - logoWidth - actionsWidth - 40 // 40px for margins

  const linksWidth = navLinks.scrollWidth

  if (linksWidth > availableWidth) {
    // 如果溢出，减小字体和间距
    navLinks.classList.add('nav-compact')
  } else {
    navLinks.classList.remove('nav-compact')
  }
}

// 快捷键处理
const handleKeydown = (event) => {
  // Ctrl/Cmd + K 打开搜索
  if ((event.ctrlKey || event.metaKey) && event.key === 'k') {
    event.preventDefault()
    globalSearch.value?.focus()
  }
}

// 添加和移除点击事件监听器
onMounted(() => {
  document.addEventListener('click', closeMenuOnOutsideClick)
  document.addEventListener('keydown', handleKeydown)
  window.addEventListener('resize', adjustNavLayout)

  // 初始化时调整布局
  setTimeout(adjustNavLayout, 500)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', closeMenuOnOutsideClick)
  document.removeEventListener('keydown', handleKeydown)
  window.removeEventListener('resize', adjustNavLayout)
})
</script>

<style scoped>
.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  position: relative;
  overflow-x: hidden;
}

/* 现代化导航栏 */
.main-nav {
  position: sticky;
  top: 0;
  z-index: 1000;
  margin: var(--spacing-md);
  margin-bottom: 0;
  border-radius: var(--radius-lg);
  animation: slideInDown 0.6s ease-out;
}

@keyframes slideInDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.nav-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 var(--spacing-lg);
  height: 80px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
}

/* Logo样式 */
.nav-logo {
  flex-shrink: 0;
}

.logo-link {
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
  padding: var(--spacing-sm) var(--spacing-md);
  border-radius: var(--radius-md);
  transition: var(--transition-normal);
  color: var(--text-primary);
}

.logo-link:hover {
  background: rgba(255, 255, 255, 0.1);
  transform: scale(1.02);
}

.logo-icon {
  width: 32px;
  height: 32px;
  color: var(--primary-color);
  transition: var(--transition-normal);
}

.logo-link:hover .logo-icon {
  color: var(--secondary-color);
  transform: rotate(5deg);
}

.logo-text {
  font-size: 1.5rem;
  font-weight: 700;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* 导航链接 */
.nav-links {
  display: flex;
  gap: var(--spacing-xs);
  flex: 1;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: var(--spacing-xs);
  padding: var(--spacing-sm) var(--spacing-md);
  border-radius: var(--radius-md);
  color: var(--text-secondary);
  font-weight: 500;
  font-size: 13px;
  transition: var(--transition-normal);
  position: relative;
  overflow: hidden;
  text-decoration: none;
  white-space: nowrap;
  flex-shrink: 1;
  min-width: 0;
  max-width: 140px;
}

.nav-link::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
  transition: var(--transition-slow);
}

.nav-link:hover::before {
  left: 100%;
}

.nav-link:hover {
  color: var(--text-primary);
  background: rgba(255, 255, 255, 0.08);
  transform: translateY(-2px);
}

.nav-link.active {
  color: var(--text-primary);
  background: linear-gradient(135deg,
    rgba(79, 172, 254, 0.2),
    rgba(67, 233, 123, 0.2));
  border: 1px solid rgba(79, 172, 254, 0.3);
  box-shadow: 0 4px 12px rgba(79, 172, 254, 0.2);
}

.link-icon {
  font-size: 16px;
  transition: var(--transition-normal);
  flex-shrink: 0;
  display: inline-block;
}

.nav-link:hover .link-icon {
  transform: scale(1.1);
}

.link-text {
  font-weight: 600;
  flex-shrink: 1;
  display: inline-block;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  min-width: 0;
}

/* 右侧操作区域 */
.nav-actions {
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
  flex-shrink: 0;
}

.action-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  border: none;
  border-radius: var(--radius-md);
  background: rgba(255, 255, 255, 0.05);
  color: var(--text-secondary);
  cursor: pointer;
  transition: var(--transition-normal);
  position: relative;
  overflow: hidden;
}

.action-btn svg {
  width: 20px;
  height: 20px;
  transition: var(--transition-normal);
}

.action-btn:hover {
  background: rgba(255, 255, 255, 0.1);
  color: var(--text-primary);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.action-btn:hover svg {
  transform: scale(1.1);
}

.notification-btn {
  position: relative;
}

.notification-badge {
  position: absolute;
  top: -2px;
  right: -2px;
  background: linear-gradient(135deg, #ef4444, #dc2626);
  color: white;
  font-size: 10px;
  font-weight: 600;
  padding: 2px 6px;
  border-radius: 10px;
  min-width: 18px;
  height: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  animation: pulse 2s infinite;
}

/* 用户区域 */
.user-section {
  position: relative;
}

.user-btn {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  padding: var(--spacing-sm) var(--spacing-md);
  border: none;
  border-radius: var(--radius-md);
  background: rgba(255, 255, 255, 0.05);
  color: var(--text-primary);
  cursor: pointer;
  transition: var(--transition-normal);
  min-width: 160px;
}

.user-btn:hover {
  background: rgba(255, 255, 255, 0.1);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.user-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  font-size: 13px;
  flex-shrink: 0;
}

.user-info-inline {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  flex: 1;
}

.user-name {
  font-weight: 600;
  font-size: 13px;
  color: var(--text-primary);
}

.user-role {
  font-size: 11px;
  color: var(--text-muted);
}

.dropdown-icon {
  width: 16px;
  height: 16px;
  transition: var(--transition-normal);
  flex-shrink: 0;
}

.dropdown-icon.rotated {
  transform: rotate(180deg);
}

/* 用户下拉菜单 */
.user-menu {
  position: fixed;
  top: 90px;
  right: var(--spacing-lg);
  width: 280px;
  border-radius: var(--radius-lg);
  overflow: hidden;
  z-index: 9999;
  animation: scaleIn 0.2s ease-out;
  box-shadow: var(--shadow-lg), 0 0 40px rgba(0, 0, 0, 0.3);
  background: rgba(30, 41, 59, 0.95);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(79, 172, 254, 0.3);
}

.menu-header {
  padding: var(--spacing-lg);
  background: linear-gradient(135deg,
    rgba(79, 172, 254, 0.15),
    rgba(67, 233, 123, 0.15));
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.user-avatar-large {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 700;
  font-size: 18px;
  flex-shrink: 0;
}

.user-details {
  flex: 1;
}

.user-details .user-name {
  font-size: 16px;
  font-weight: 700;
  margin-bottom: 4px;
  color: var(--text-primary);
}

.user-email {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: 8px;
}

.menu-divider {
  height: 1px;
  background: rgba(255, 255, 255, 0.15);
  margin: 0;
}

.menu-items {
  padding: var(--spacing-sm);
}

.menu-item {
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
  padding: var(--spacing-md);
  border-radius: var(--radius-md);
  color: rgba(255, 255, 255, 0.9);
  cursor: pointer;
  transition: var(--transition-normal);
  margin-bottom: var(--spacing-xs);
  font-weight: 500;
}

.menu-item:hover {
  background: rgba(79, 172, 254, 0.15);
  color: var(--text-primary);
  transform: translateX(4px);
  box-shadow: 0 2px 8px rgba(79, 172, 254, 0.2);
}

.menu-item.logout-item {
  color: var(--error-color);
}

.menu-item.logout-item:hover {
  background: rgba(239, 68, 68, 0.1);
  color: var(--error-color);
}

.menu-icon {
  width: 18px;
  height: 18px;
  flex-shrink: 0;
}

/* 用户角色标签 */
.badge {
  display: inline-block;
  padding: 2px 8px;
  border-radius: var(--radius-sm);
  font-size: 10px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.badge-primary {
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  color: white;
}

/* 下拉动画 */
.dropdown-enter-active,
.dropdown-leave-active {
  transition: all 0.3s ease;
}

.dropdown-enter-from {
  opacity: 0;
  transform: translateY(-10px) scale(0.95);
}

.dropdown-leave-to {
  opacity: 0;
  transform: translateY(-10px) scale(0.95);
}

/* 主内容区域 */
.main-content {
  flex: 1;
  width: 100%;
  position: relative;
  z-index: 1;
}

/* 背景装饰 */
.bg-decoration {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
  overflow: hidden;
}

.decoration-circle {
  position: absolute;
  border-radius: 50%;
  background: linear-gradient(135deg,
    rgba(79, 172, 254, 0.1),
    rgba(67, 233, 123, 0.1));
  animation: float 6s ease-in-out infinite;
}

.circle-1 {
  width: 300px;
  height: 300px;
  top: 10%;
  right: -150px;
  animation-delay: 0s;
}

.circle-2 {
  width: 200px;
  height: 200px;
  bottom: 20%;
  left: -100px;
  animation-delay: 2s;
}

.circle-3 {
  width: 150px;
  height: 150px;
  top: 60%;
  right: 10%;
  animation-delay: 4s;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0px) rotate(0deg);
  }
  50% {
    transform: translateY(-20px) rotate(180deg);
  }
}

/* 语言适配 - 针对较长的文本 */
.nav-link {
  transition: all 0.3s ease;
}

/* 语言特定的导航栏样式 */
[lang="en"] .nav-links,
[lang="en-US"] .nav-links {
  gap: var(--spacing-xs);
}

[lang="en"] .nav-link,
[lang="en-US"] .nav-link {
  font-size: 12px;
  padding: var(--spacing-sm) var(--spacing-md);
}

[lang="ja"] .nav-links,
[lang="ja-JP"] .nav-links {
  gap: 2px;
}

[lang="ja"] .nav-link,
[lang="ja-JP"] .nav-link {
  font-size: 12px;
  padding: var(--spacing-sm) var(--spacing-sm);
  max-width: 120px;
}

[lang="zh"] .nav-links,
[lang="zh-CN"] .nav-links {
  gap: var(--spacing-sm);
}

[lang="zh"] .nav-link,
[lang="zh-CN"] .nav-link {
  font-size: 14px;
  padding: var(--spacing-md) var(--spacing-lg);
}

/* 紧凑模式 - 当导航栏空间不足时 */
.nav-links.nav-compact {
  gap: 2px;
}

.nav-links.nav-compact .nav-link {
  font-size: 11px;
  padding: var(--spacing-sm) var(--spacing-xs);
  max-width: 80px;
}

.nav-links.nav-compact .link-text {
  font-size: 11px;
}

/* 当文本较长时的样式调整 */
@media (min-width: 1200px) {
  .nav-link {
    max-width: 160px;
    padding: var(--spacing-md) var(--spacing-lg);
  }

  .nav-links {
    gap: var(--spacing-sm);
  }
}

/* 中等屏幕优化 */
@media (max-width: 1199px) and (min-width: 1025px) {
  .nav-link {
    max-width: 130px;
    font-size: 12px;
  }

  .link-text {
    font-size: 12px;
  }
}

/* 响应式设计 */
@media (max-width: 1024px) {
  .nav-container {
    padding: 0 var(--spacing-md);
  }

  .user-btn {
    min-width: auto;
  }

  .user-info-inline {
    display: none;
  }

  .nav-link {
    max-width: 100px;
    font-size: 11px;
    padding: var(--spacing-sm);
  }

  .link-text {
    font-size: 11px;
  }
}

@media (max-width: 768px) {
  .main-nav {
    margin: var(--spacing-sm);
    margin-bottom: 0;
  }

  .nav-container {
    height: auto;
    padding: var(--spacing-md);
    flex-direction: row;
    flex-wrap: wrap;
    gap: var(--spacing-md);
  }

  .nav-logo {
    order: 1;
  }

  .nav-actions {
    order: 2;
    margin-left: auto;
  }

  .nav-links {
    order: 3;
    width: 100%;
    justify-content: flex-start;
    overflow-x: auto;
    padding-bottom: var(--spacing-sm);
    gap: var(--spacing-xs);
    scrollbar-width: none;
    -ms-overflow-style: none;
  }

  .nav-links::-webkit-scrollbar {
    display: none;
  }

  .nav-link {
    white-space: nowrap;
    padding: var(--spacing-sm) var(--spacing-md);
    flex-shrink: 0;
  }

  .link-text {
    display: none;
  }

  .user-menu {
    position: fixed;
    top: 120px;
    right: var(--spacing-md);
    left: var(--spacing-md);
    width: auto;
  }

  .decoration-circle {
    display: none;
  }
}

@media (max-width: 480px) {
  .logo-text {
    font-size: 1.2rem;
  }

  .nav-container {
    padding: var(--spacing-sm);
  }

  .nav-links {
    gap: var(--spacing-xs);
    padding-bottom: var(--spacing-xs);
  }

  .nav-link {
    padding: var(--spacing-sm);
    min-width: 44px;
    justify-content: center;
  }

  .link-icon {
    font-size: 18px;
  }
}

/* 浅色主题下的导航栏优化 */
.light-theme .logo-text {
  background: linear-gradient(135deg, #1e40af, #7c3aed) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  background-clip: text !important;
  font-weight: 800 !important;
}

.light-theme .nav-link {
  color: #1a202c !important;
  font-weight: 600 !important;
}

.light-theme .nav-link:hover {
  color: #000000 !important;
  background: rgba(0, 0, 0, 0.05) !important;
}

.light-theme .nav-link.active {
  color: #000000 !important;
  background: linear-gradient(135deg, rgba(30, 64, 175, 0.15), rgba(124, 58, 237, 0.15)) !important;
  border: 1px solid rgba(30, 64, 175, 0.3) !important;
}

.light-theme .user-name {
  color: #000000 !important;
  font-weight: 700 !important;
}

.light-theme .user-role {
  color: #2d3748 !important;
  font-weight: 600 !important;
}

.light-theme .user-email {
  color: #475569 !important;
  font-weight: 500 !important;
}

.light-theme .menu-item {
  color: #1a202c !important;
  font-weight: 600 !important;
}

.light-theme .menu-item:hover {
  color: #000000 !important;
  background: rgba(30, 64, 175, 0.1) !important;
}

.light-theme .menu-item.logout-item {
  color: #b91c1c !important;
}

.light-theme .menu-item.logout-item:hover {
  background: rgba(185, 28, 28, 0.1) !important;
  color: #b91c1c !important;
}

.light-theme .action-btn {
  color: #1a202c !important;
  background: rgba(0, 0, 0, 0.05) !important;
}

.light-theme .action-btn:hover {
  color: #000000 !important;
  background: rgba(0, 0, 0, 0.1) !important;
}

.light-theme .user-btn {
  color: #000000 !important;
  background: rgba(0, 0, 0, 0.05) !important;
  font-weight: 700 !important;
}

.light-theme .user-btn:hover {
  background: rgba(0, 0, 0, 0.1) !important;
}

.light-theme .user-menu {
  background: rgba(255, 255, 255, 0.98) !important;
  border: 1px solid rgba(0, 0, 0, 0.15) !important;
}

.light-theme .menu-header {
  background: linear-gradient(135deg, rgba(30, 64, 175, 0.1), rgba(124, 58, 237, 0.1)) !important;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1) !important;
}

.light-theme .menu-divider {
  background: rgba(0, 0, 0, 0.1) !important;
}
</style>