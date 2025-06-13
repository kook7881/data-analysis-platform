<template>
  <div class="settings-container">
    <!-- 页面头部 -->
    <div class="page-header">
      <div class="header-content">
        <!-- 导航栏 -->
        <div class="page-navigation">
          <button class="back-btn" @click="goBack" title="返回">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M19 12H5m7-7l-7 7 7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span>返回</span>
          </button>

          <!-- 面包屑导航 -->
          <nav class="breadcrumb">
            <router-link to="/" class="breadcrumb-item">首页</router-link>
            <span class="breadcrumb-separator">/</span>
            <span class="breadcrumb-item current">系统设置</span>
          </nav>

          <!-- 快捷导航 -->
          <div class="quick-nav">
            <router-link to="/profile" class="quick-nav-btn">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <span>个人资料</span>
            </router-link>
          </div>
        </div>

        <!-- 页面标题 -->
        <div class="title-section">
          <h1 class="page-title">
            <svg class="title-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            系统设置
          </h1>
          <p class="page-subtitle">个性化您的使用体验</p>
        </div>
      </div>
    </div>

    <!-- 设置内容 -->
    <div class="settings-content">
      <!-- 外观设置 -->
      <div class="settings-card glass-card">
        <h3 class="card-title">
          <svg class="title-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          外观设置
        </h3>

        <div class="setting-group">
          <div class="setting-item">
            <div class="setting-info">
              <label class="setting-label">主题模式</label>
              <p class="setting-description">选择您喜欢的界面主题</p>
            </div>
            <div class="theme-selector">
              <button
                v-for="theme in themes"
                :key="theme.value"
                :class="['theme-option', { active: settingsStore.theme === theme.value }]"
                @click="updateSetting('theme', theme.value)"
              >
                <div class="theme-preview" :style="{ background: theme.preview }"></div>
                <span class="theme-name">{{ theme.name }}</span>
              </button>
            </div>
          </div>

          <div class="setting-item">
            <div class="setting-info">
              <label class="setting-label">界面语言</label>
              <p class="setting-description">选择界面显示语言</p>
            </div>
            <select :value="settingsStore.language" @change="updateSetting('language', $event.target.value)" class="setting-select clean-select">
              <option value="zh-CN">简体中文</option>
              <option value="en-US">English</option>
              <option value="ja-JP">日本語</option>
            </select>
          </div>

          <div class="setting-item">
            <div class="setting-info">
              <label class="setting-label">动画效果</label>
              <p class="setting-description">启用或禁用界面动画</p>
            </div>
            <label class="toggle-switch">
              <input
                type="checkbox"
                :checked="settingsStore.animations"
                @change="updateSetting('animations', $event.target.checked)"
              >
              <span class="toggle-slider"></span>
            </label>
          </div>
        </div>
      </div>

      <!-- 数据设置 -->
      <div class="settings-card glass-card">
        <h3 class="card-title">
          <svg class="title-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          数据设置
        </h3>

        <div class="setting-group">
          <div class="setting-item">
            <div class="setting-info">
              <label class="setting-label">自动刷新</label>
              <p class="setting-description">自动刷新数据的时间间隔</p>
            </div>
            <select :value="settingsStore.autoRefresh" @change="updateSetting('autoRefresh', parseInt($event.target.value))" class="setting-select clean-select">
              <option value="0">关闭</option>
              <option value="30">30秒</option>
              <option value="60">1分钟</option>
              <option value="300">5分钟</option>
              <option value="600">10分钟</option>
            </select>
          </div>

          <div class="setting-item">
            <div class="setting-info">
              <label class="setting-label">数据缓存</label>
              <p class="setting-description">启用数据缓存以提高性能</p>
            </div>
            <label class="toggle-switch">
              <input
                type="checkbox"
                :checked="settingsStore.dataCache"
                @change="updateSetting('dataCache', $event.target.checked)"
              >
              <span class="toggle-slider"></span>
            </label>
          </div>

          <div class="setting-item">
            <div class="setting-info">
              <label class="setting-label">实时数据</label>
              <p class="setting-description">启用实时数据推送</p>
            </div>
            <label class="toggle-switch">
              <input
                type="checkbox"
                :checked="settingsStore.realTimeData"
                @change="updateSetting('realTimeData', $event.target.checked)"
              >
              <span class="toggle-slider"></span>
            </label>
          </div>
        </div>
      </div>

      <!-- 通知设置 -->
      <div class="settings-card glass-card">
        <h3 class="card-title">
          <svg class="title-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M18 8A6 6 0 006 8c0 7-3 9-3 9h18s-3-2-3-9M13.73 21a2 2 0 01-3.46 0" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          通知设置
        </h3>

        <div class="setting-group">
          <div class="setting-item">
            <div class="setting-info">
              <label class="setting-label">桌面通知</label>
              <p class="setting-description">允许显示桌面通知</p>
            </div>
            <label class="toggle-switch">
              <input
                type="checkbox"
                :checked="settingsStore.desktopNotifications"
                @change="updateSetting('desktopNotifications', $event.target.checked)"
              >
              <span class="toggle-slider"></span>
            </label>
          </div>

          <div class="setting-item">
            <div class="setting-info">
              <label class="setting-label">邮件通知</label>
              <p class="setting-description">接收重要事件的邮件通知</p>
            </div>
            <label class="toggle-switch">
              <input
                type="checkbox"
                :checked="settingsStore.emailNotifications"
                @change="updateSetting('emailNotifications', $event.target.checked)"
              >
              <span class="toggle-slider"></span>
            </label>
          </div>

          <div class="setting-item">
            <div class="setting-info">
              <label class="setting-label">声音提示</label>
              <p class="setting-description">播放通知声音</p>
            </div>
            <label class="toggle-switch">
              <input
                type="checkbox"
                :checked="settingsStore.soundNotifications"
                @change="updateSetting('soundNotifications', $event.target.checked)"
              >
              <span class="toggle-slider"></span>
            </label>
          </div>
        </div>
      </div>

      <!-- 安全设置 -->
      <div class="settings-card glass-card">
        <h3 class="card-title">
          <svg class="title-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          安全设置
        </h3>

        <div class="setting-group">
          <div class="setting-item">
            <div class="setting-info">
              <label class="setting-label">自动登出</label>
              <p class="setting-description">无操作时自动登出的时间</p>
            </div>
            <select :value="settingsStore.autoLogout" @change="updateSetting('autoLogout', parseInt($event.target.value))" class="setting-select clean-select">
              <option value="0">从不</option>
              <option value="15">15分钟</option>
              <option value="30">30分钟</option>
              <option value="60">1小时</option>
              <option value="120">2小时</option>
            </select>
          </div>

          <div class="setting-item">
            <div class="setting-info">
              <label class="setting-label">双因素认证</label>
              <p class="setting-description">启用双因素身份验证</p>
            </div>
            <label class="toggle-switch">
              <input
                type="checkbox"
                :checked="settingsStore.twoFactorAuth"
                @change="updateSetting('twoFactorAuth', $event.target.checked)"
              >
              <span class="toggle-slider"></span>
            </label>
          </div>

          <div class="setting-item">
            <div class="setting-info">
              <label class="setting-label">登录历史</label>
              <p class="setting-description">记录登录历史记录</p>
            </div>
            <label class="toggle-switch">
              <input
                type="checkbox"
                :checked="settingsStore.loginHistory"
                @change="updateSetting('loginHistory', $event.target.checked)"
              >
              <span class="toggle-slider"></span>
            </label>
          </div>
        </div>
      </div>

      <!-- 操作按钮 -->
      <div class="settings-actions">
        <button class="btn btn-primary" @click="saveSettings" :disabled="saving">
          <span v-if="saving" class="loading-spinner"></span>
          <span>{{ saving ? '保存中...' : '保存设置' }}</span>
        </button>
        <button class="btn btn-secondary" @click="resetSettings">
          重置为默认
        </button>
        <button class="btn btn-danger" @click="clearCache">
          清除缓存
        </button>
      </div>
    </div>

    <!-- 状态提示 -->
    <transition name="alert">
      <div v-if="alert.show" :class="['alert', `alert-${alert.type}`]">
        <div class="alert-icon">
          <svg v-if="alert.type === 'success'" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <svg v-else-if="alert.type === 'error'" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 9v3.75m9-.75a9 9 0 11-18 0 9 9 0 0118 0zm-9 3.75h.008v.008H12v-.008z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <span class="alert-message">{{ alert.message }}</span>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { useSettingsStore } from '../store'

const router = useRouter()
const { t } = useI18n()
const settingsStore = useSettingsStore()
const saving = ref(false)

// 状态提示
const alert = reactive({
  show: false,
  type: 'info',
  message: ''
})

// 主题选项
const themes = [
  { name: '深色', value: 'dark', preview: 'linear-gradient(135deg, #1a1a2e, #16213e)' },
  { name: '浅色', value: 'light', preview: 'linear-gradient(135deg, #f8f9fa, #e9ecef)' },
  { name: '自动', value: 'auto', preview: 'linear-gradient(135deg, #4facfe, #00f2fe)' }
]

// 使用store中的设置数据
const settings = computed(() => settingsStore.getAllSettings)

// 显示提示消息
const showAlert = (type, message) => {
  alert.show = true
  alert.type = type
  alert.message = message

  setTimeout(() => {
    alert.show = false
  }, 3000)
}

// 更新单个设置
const updateSetting = async (key, value) => {
  try {
    await settingsStore.updateSetting(key, value)
    showAlert('success', t('settings.messages.updated'))

    // 如果是语言设置，立即应用
    if (key === 'language') {
      // 强制重新渲染页面以应用新语言
      setTimeout(() => {
        window.location.reload()
      }, 500)
    }
  } catch (error) {
    console.error('更新设置失败:', error)
    showAlert('error', t('settings.messages.updateFailed'))
  }
}

// 保存设置
const saveSettings = async () => {
  saving.value = true
  try {
    await settingsStore.saveSettings()
    showAlert('success', '设置保存成功！')
  } catch (error) {
    console.error('保存设置失败:', error)
    showAlert('error', '保存失败，请稍后重试')
  } finally {
    saving.value = false
  }
}

// 重置设置
const resetSettings = async () => {
  try {
    await settingsStore.resetSettings()
    showAlert('success', '设置已重置为默认值')
  } catch (error) {
    console.error('重置设置失败:', error)
    showAlert('error', '重置设置失败')
  }
}

// 清除缓存
const clearCache = async () => {
  try {
    // 清除本地存储中的缓存数据
    const keysToRemove = []
    for (let i = 0; i < localStorage.length; i++) {
      const key = localStorage.key(i)
      if (key && (key.startsWith('cache_') || key.startsWith('data_'))) {
        keysToRemove.push(key)
      }
    }

    keysToRemove.forEach(key => localStorage.removeItem(key))

    showAlert('success', '缓存清除成功！')
  } catch (error) {
    console.error('清除缓存失败:', error)
    showAlert('error', '清除缓存失败')
  }
}

// 返回上一页
const goBack = () => {
  if (window.history.length > 1) {
    router.go(-1)
  } else {
    router.push('/')
  }
}

// 组件挂载时加载设置
onMounted(async () => {
  try {
    await settingsStore.loadSettings()
  } catch (error) {
    console.error('加载设置失败:', error)
    showAlert('error', '加载设置失败')
  }
})
</script>

<style scoped>
.settings-container {
  min-height: 100vh;
  background: var(--bg-primary);
  padding: var(--spacing-xl);
}

/* 页面头部 */
.page-header {
  margin-bottom: var(--spacing-2xl);
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
}

/* 页面导航 */
.page-navigation {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--spacing-xl);
  padding-bottom: var(--spacing-lg);
  border-bottom: 1px solid var(--border-color);
}

.back-btn {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  padding: var(--spacing-sm) var(--spacing-md);
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  color: var(--text-secondary);
  cursor: pointer;
  transition: var(--transition-normal);
  font-size: 0.9rem;
  font-weight: 500;
}

.back-btn:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: var(--border-hover);
  color: var(--text-primary);
  transform: translateX(-2px);
}

.back-btn svg {
  width: 18px;
  height: 18px;
}

/* 面包屑导航 */
.breadcrumb {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  font-size: 0.9rem;
}

.breadcrumb-item {
  color: var(--text-secondary);
  text-decoration: none;
  transition: var(--transition-normal);
}

.breadcrumb-item:hover {
  color: var(--primary-color);
}

.breadcrumb-item.current {
  color: var(--text-primary);
  font-weight: 600;
}

.breadcrumb-separator {
  color: var(--text-muted);
  font-weight: 300;
}

/* 快捷导航 */
.quick-nav {
  display: flex;
  gap: var(--spacing-sm);
}

.quick-nav-btn {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  padding: var(--spacing-sm) var(--spacing-md);
  background: rgba(79, 172, 254, 0.1);
  border: 1px solid rgba(79, 172, 254, 0.3);
  border-radius: var(--radius-md);
  color: var(--primary-color);
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  transition: var(--transition-normal);
}

.quick-nav-btn:hover {
  background: rgba(79, 172, 254, 0.2);
  border-color: var(--primary-color);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.quick-nav-btn svg {
  width: 16px;
  height: 16px;
}

/* 标题区域 */
.title-section {
  margin-top: var(--spacing-lg);
}

.page-title {
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
  font-size: 2rem;
  font-weight: 700;
  color: #ffffff;
  margin: 0 0 var(--spacing-sm) 0;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
  letter-spacing: -0.02em;
}

.title-icon {
  width: 32px;
  height: 32px;
  color: var(--primary-color);
  filter: drop-shadow(0 2px 4px rgba(79, 172, 254, 0.3));
}

.page-subtitle {
  font-size: 1rem;
  color: rgba(255, 255, 255, 0.9);
  margin: 0;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

/* 设置内容 */
.settings-content {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  gap: var(--spacing-xl);
}

/* 设置卡片 */
.settings-card {
  padding: var(--spacing-2xl);
  background: var(--bg-glass);
  backdrop-filter: blur(20px);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
  transition: var(--transition-normal);
}

.settings-card:hover {
  border-color: var(--border-hover);
  box-shadow: var(--shadow-glow);
}

.card-title {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  font-size: 1.3rem;
  font-weight: 600;
  color: #ffffff;
  margin: 0 0 var(--spacing-xl) 0;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5);
  letter-spacing: -0.01em;
}

.card-title .title-icon {
  width: 24px;
  height: 24px;
  color: var(--primary-color);
  filter: drop-shadow(0 1px 2px rgba(79, 172, 254, 0.3));
}

/* 设置组 */
.setting-group {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-lg);
}

.setting-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--spacing-lg);
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  transition: var(--transition-normal);
}

.setting-item:hover {
  background: rgba(255, 255, 255, 0.05);
  border-color: var(--border-hover);
}

.setting-info {
  flex: 1;
}

.setting-label {
  font-size: 1rem;
  font-weight: 600;
  color: #ffffff;
  margin: 0 0 var(--spacing-xs) 0;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
  letter-spacing: 0.01em;
}

.setting-description {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.8);
  margin: 0;
  line-height: 1.4;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}

/* 主题选择器 */
.theme-selector {
  display: flex;
  gap: var(--spacing-sm);
}

.theme-option {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--spacing-xs);
  padding: var(--spacing-sm);
  background: transparent;
  border: 2px solid var(--border-color);
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: var(--transition-normal);
}

.theme-option:hover {
  border-color: var(--border-hover);
}

.theme-option.active {
  border-color: var(--primary-color);
  background: rgba(79, 172, 254, 0.1);
}

.theme-preview {
  width: 40px;
  height: 24px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-color);
}

.theme-name {
  font-size: 0.8rem;
  color: rgba(255, 255, 255, 0.8);
  font-weight: 500;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

/* 选择框 */
.setting-select {
  padding: var(--spacing-sm) var(--spacing-md);
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: var(--radius-md);
  color: #ffffff !important;
  font-size: 14px;
  font-weight: 500;
  min-width: 120px;
  transition: var(--transition-normal);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  font-family: var(--font-family);
  line-height: 1.4;
  letter-spacing: 0;
  text-rendering: optimizeLegibility;
  background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6,9 12,15 18,9'%3e%3c/polyline%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right 8px center;
  background-size: 14px;
  padding-right: 32px;
}

.setting-select:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(79, 172, 254, 0.1);
}

/* 下拉框选项样式 */
.setting-select option {
  background: #1e293b;
  color: #ffffff;
  padding: 8px 12px;
  font-weight: 500;
  border: none;
  font-family: var(--font-family);
  font-size: 14px;
  line-height: 1.4;
  letter-spacing: 0;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.setting-select option:hover {
  background: #334155;
}

.setting-select option:checked {
  background: var(--primary-color);
  color: #ffffff;
}

/* 切换开关 */
.toggle-switch {
  position: relative;
  display: inline-block;
  width: 50px;
  height: 24px;
  cursor: pointer;
}

.toggle-switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.toggle-slider {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 24px;
  transition: var(--transition-normal);
}

.toggle-slider:before {
  position: absolute;
  content: "";
  height: 18px;
  width: 18px;
  left: 2px;
  bottom: 2px;
  background: white;
  border-radius: 50%;
  transition: var(--transition-normal);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.toggle-switch input:checked + .toggle-slider {
  background: var(--primary-color);
  border-color: var(--primary-color);
}

.toggle-switch input:checked + .toggle-slider:before {
  transform: translateX(26px);
}

/* 操作按钮 */
.settings-actions {
  display: flex;
  gap: var(--spacing-md);
  justify-content: center;
  margin-top: var(--spacing-2xl);
  padding-top: var(--spacing-xl);
  border-top: 1px solid var(--border-color);
}

.btn {
  padding: var(--spacing-md) var(--spacing-xl);
  border: none;
  border-radius: var(--radius-md);
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition-normal);
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  text-decoration: none;
}

.btn-primary {
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  color: white;
  box-shadow: var(--shadow-md);
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

.btn-primary:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.btn-secondary {
  background: var(--bg-glass);
  color: var(--text-primary);
  border: 1px solid var(--border-color);
}

.btn-secondary:hover {
  background: var(--bg-hover);
  border-color: var(--border-hover);
}

.btn-danger {
  background: linear-gradient(135deg, var(--error-color), #dc2626);
  color: white;
  box-shadow: var(--shadow-md);
}

.btn-danger:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

/* 加载动画 */
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

/* 状态提示 */
.alert {
  position: fixed;
  top: var(--spacing-xl);
  right: var(--spacing-xl);
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  padding: var(--spacing-md) var(--spacing-lg);
  border-radius: var(--radius-md);
  font-size: 0.9rem;
  font-weight: 500;
  backdrop-filter: blur(10px);
  box-shadow: var(--shadow-lg);
  z-index: 1000;
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
  transform: translateX(100px);
}

/* 浅色主题下的设置页面样式优化 */
.light-theme .page-title {
  color: #0f172a !important;
  text-shadow: 0 2px 4px rgba(255, 255, 255, 0.8) !important;
}

.light-theme .page-subtitle {
  color: #475569 !important;
  text-shadow: 0 1px 2px rgba(255, 255, 255, 0.6) !important;
}

.light-theme .card-title {
  color: #0f172a !important;
  text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8) !important;
}

.light-theme .setting-label {
  color: #0f172a !important;
  text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8) !important;
  font-weight: 700 !important;
}

.light-theme .setting-description {
  color: #475569 !important;
  text-shadow: 0 1px 2px rgba(255, 255, 255, 0.6) !important;
  font-weight: 500 !important;
}

.light-theme .theme-name {
  color: #475569 !important;
  text-shadow: 0 1px 2px rgba(255, 255, 255, 0.6) !important;
  font-weight: 600 !important;
}

.light-theme .setting-select {
  color: #0f172a !important;
  background: rgba(0, 0, 0, 0.05) !important;
  border: 1px solid rgba(0, 0, 0, 0.15) !important;
  text-shadow: none !important;
  font-weight: 600 !important;
  background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%230f172a' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6,9 12,15 18,9'%3e%3c/polyline%3e%3c/svg%3e") !important;
}

.light-theme .setting-select:focus {
  border-color: #2563eb !important;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1) !important;
}

/* 浅色主题下的下拉框选项样式 */
.light-theme .setting-select option {
  background: #ffffff !important;
  color: #000000 !important;
  font-weight: 600 !important;
  padding: 8px 12px !important;
  border: none !important;
}

.light-theme .setting-select option:hover {
  background: #f1f5f9 !important;
  color: #000000 !important;
}

.light-theme .setting-select option:checked,
.light-theme .setting-select option:selected {
  background: #2563eb !important;
  color: #ffffff !important;
  font-weight: 700 !important;
}

/* 确保下拉框在浅色主题下的文字可见性 */
.light-theme select {
  color: #000000 !important;
  background: rgba(255, 255, 255, 0.9) !important;
  border: 1px solid rgba(0, 0, 0, 0.2) !important;
  font-weight: 600 !important;
}

.light-theme select:focus {
  border-color: #2563eb !important;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1) !important;
}

.light-theme .breadcrumb-item {
  color: #475569 !important;
  font-weight: 600 !important;
}

.light-theme .breadcrumb-item.current {
  color: #0f172a !important;
  font-weight: 700 !important;
}

.light-theme .breadcrumb-separator {
  color: #64748b !important;
}

.light-theme .back-btn {
  color: #475569 !important;
  background: rgba(0, 0, 0, 0.03) !important;
  border: 1px solid rgba(0, 0, 0, 0.1) !important;
  font-weight: 600 !important;
}

.light-theme .back-btn:hover {
  color: #0f172a !important;
  background: rgba(0, 0, 0, 0.05) !important;
  border-color: rgba(37, 99, 235, 0.3) !important;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .settings-container {
    padding: var(--spacing-lg);
  }

  .page-navigation {
    flex-direction: column;
    gap: var(--spacing-md);
    align-items: stretch;
  }

  .breadcrumb {
    justify-content: center;
  }

  .quick-nav {
    justify-content: center;
  }

  .settings-card {
    padding: var(--spacing-lg);
  }

  .setting-item {
    flex-direction: column;
    align-items: flex-start;
    gap: var(--spacing-md);
  }

  .theme-selector {
    width: 100%;
    justify-content: space-between;
  }

  .settings-actions {
    flex-direction: column;
    align-items: center;
  }

  .btn {
    width: 100%;
    justify-content: center;
  }
}

@media (max-width: 480px) {
  .settings-container {
    padding: var(--spacing-md);
  }

  .page-title {
    font-size: 1.5rem;
  }

  .theme-option {
    flex: 1;
  }

  .theme-preview {
    width: 100%;
    height: 20px;
  }
}

/* 完全重置的下拉框样式 - 解决符号显示问题 */
.clean-select {
  /* 重置所有样式 */
  all: unset !important;

  /* 基础样式 */
  display: inline-block !important;
  width: auto !important;
  min-width: 120px !important;
  padding: 8px 32px 8px 12px !important;
  margin: 0 !important;

  /* 字体设置 */
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif !important;
  font-size: 14px !important;
  font-weight: 500 !important;
  line-height: 1.4 !important;

  /* 颜色和背景 */
  color: #ffffff !important;
  background-color: rgba(255, 255, 255, 0.08) !important;

  /* 边框 */
  border: 1px solid rgba(255, 255, 255, 0.2) !important;
  border-radius: 8px !important;

  /* 其他 */
  cursor: pointer !important;
  transition: all 0.2s ease !important;

  /* 下拉箭头 */
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3e%3cpath stroke='%23ffffff' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.5' d='M6 8l4 4 4-4'/%3e%3c/svg%3e") !important;
  background-position: right 8px center !important;
  background-repeat: no-repeat !important;
  background-size: 16px !important;

  /* 移除默认样式 */
  -webkit-appearance: none !important;
  -moz-appearance: none !important;
  appearance: none !important;
}

.clean-select:focus {
  outline: none !important;
  border-color: var(--primary-color) !important;
  box-shadow: 0 0 0 3px rgba(79, 172, 254, 0.1) !important;
}

.clean-select option {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif !important;
  font-size: 14px !important;
  font-weight: 500 !important;
  color: #000000 !important;
  background-color: #ffffff !important;
  padding: 8px 12px !important;
}

/* 浅色主题下的clean-select - 特殊处理字体显示问题 */
.light-theme .clean-select {
  /* 完全重置 */
  all: unset !important;

  /* 重新定义基础样式 */
  display: inline-block !important;
  width: auto !important;
  min-width: 120px !important;
  padding: 8px 32px 8px 12px !important;
  margin: 0 !important;

  /* 强制使用系统字体 */
  font-family: "Microsoft YaHei", "微软雅黑", "PingFang SC", "Hiragino Sans GB", "Segoe UI", Arial, sans-serif !important;
  font-size: 14px !important;
  font-weight: 600 !important;
  line-height: 1.4 !important;

  /* 颜色设置 */
  color: #000000 !important;
  background-color: #ffffff !important;
  border: 2px solid rgba(0, 0, 0, 0.2) !important;
  border-radius: 8px !important;

  /* 移除所有可能导致问题的样式 */
  text-shadow: none !important;
  text-transform: none !important;
  letter-spacing: 0 !important;
  word-spacing: 0 !important;
  font-variant: normal !important;
  font-feature-settings: normal !important;
  -webkit-font-feature-settings: normal !important;
  font-synthesis: none !important;
  -webkit-text-stroke: 0 !important;

  /* 字体渲染优化 */
  -webkit-font-smoothing: antialiased !important;
  -moz-osx-font-smoothing: grayscale !important;
  text-rendering: optimizeLegibility !important;

  /* 下拉箭头 */
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3e%3cpath stroke='%23000000' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.5' d='M6 8l4 4 4-4'/%3e%3c/svg%3e") !important;
  background-position: right 8px center !important;
  background-repeat: no-repeat !important;
  background-size: 16px !important;

  /* 移除默认样式 */
  -webkit-appearance: none !important;
  -moz-appearance: none !important;
  appearance: none !important;

  /* 其他 */
  cursor: pointer !important;
  transition: all 0.2s ease !important;
}

.light-theme .clean-select:focus {
  border-color: #1e40af !important;
  box-shadow: 0 0 0 3px rgba(30, 64, 175, 0.1) !important;
  outline: none !important;
}

.light-theme .clean-select option {
  font-family: "Microsoft YaHei", "微软雅黑", "PingFang SC", "Hiragino Sans GB", "Segoe UI", Arial, sans-serif !important;
  font-size: 14px !important;
  font-weight: 600 !important;
  color: #000000 !important;
  background-color: #ffffff !important;
  padding: 8px 12px !important;
  text-shadow: none !important;
  font-variant: normal !important;
  font-feature-settings: normal !important;
  -webkit-font-feature-settings: normal !important;
  font-synthesis: none !important;
  -webkit-text-stroke: 0 !important;
}
</style>
