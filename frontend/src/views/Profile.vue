<template>
  <div class="profile-container">
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
            <span class="breadcrumb-item current">个人资料</span>
          </nav>

          <!-- 快捷导航 -->
          <div class="quick-nav">
            <router-link to="/settings" class="quick-nav-btn">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <span>设置</span>
            </router-link>
          </div>
        </div>

        <!-- 页面标题 -->
        <div class="title-section">
          <h1 class="page-title">
            <svg class="title-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            个人资料
          </h1>
          <p class="page-subtitle">管理您的个人信息和账户设置</p>
        </div>
      </div>
    </div>

    <!-- 主要内容 -->
    <div class="profile-content">
      <!-- 用户信息卡片 -->
      <div class="profile-card glass-card">
        <div class="profile-header">
          <div class="avatar-section">
            <div class="avatar-container">
              <div class="user-avatar" :style="{ backgroundColor: avatarColor }">
                {{ userInitial }}
              </div>
              <button class="avatar-upload-btn" @click="triggerAvatarUpload">
                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M12 16v-4m0 0V8m0 4h4m-4 0H8m12 8H4a2 2 0 01-2-2V6a2 2 0 012-2h16a2 2 0 012 2v14a2 2 0 01-2 2z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
              <input ref="avatarInput" type="file" accept="image/*" @change="handleAvatarChange" style="display: none;">
            </div>
          </div>
          <div class="user-info">
            <h2 class="user-name">{{ userProfile.username }}</h2>
            <p class="user-role">{{ userProfile.role === 'admin' ? '管理员' : '普通用户' }}</p>
            <p class="user-email">{{ userProfile.email }}</p>
          </div>
        </div>

        <!-- 个人信息表单 -->
        <div class="profile-form">
          <h3 class="form-title">基本信息</h3>
          
          <form @submit.prevent="updateProfile">
            <div class="form-row">
              <div class="form-group">
                <label class="form-label">用户名</label>
                <input 
                  v-model="profileForm.username" 
                  type="text" 
                  class="form-input"
                  placeholder="请输入用户名"
                  required
                >
              </div>
              <div class="form-group">
                <label class="form-label">邮箱地址</label>
                <input 
                  v-model="profileForm.email" 
                  type="email" 
                  class="form-input"
                  placeholder="请输入邮箱地址"
                  required
                >
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label class="form-label">真实姓名</label>
                <input 
                  v-model="profileForm.realName" 
                  type="text" 
                  class="form-input"
                  placeholder="请输入真实姓名"
                >
              </div>
              <div class="form-group">
                <label class="form-label">手机号码</label>
                <input 
                  v-model="profileForm.phone" 
                  type="tel" 
                  class="form-input"
                  placeholder="请输入手机号码"
                >
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label class="form-label">部门</label>
                <select v-model="profileForm.department" class="form-select">
                  <option value="">请选择部门</option>
                  <option value="技术部">技术部</option>
                  <option value="产品部">产品部</option>
                  <option value="运营部">运营部</option>
                  <option value="市场部">市场部</option>
                  <option value="财务部">财务部</option>
                  <option value="人事部">人事部</option>
                </select>
              </div>
              <div class="form-group">
                <label class="form-label">职位</label>
                <input 
                  v-model="profileForm.position" 
                  type="text" 
                  class="form-input"
                  placeholder="请输入职位"
                >
              </div>
            </div>

            <div class="form-group">
              <label class="form-label">个人简介</label>
              <textarea 
                v-model="profileForm.bio" 
                class="form-textarea"
                placeholder="请输入个人简介"
                rows="4"
              ></textarea>
            </div>

            <div class="form-actions">
              <button type="submit" class="btn btn-primary" :disabled="loading">
                <span v-if="loading" class="loading-spinner"></span>
                <span>{{ loading ? '保存中...' : '保存更改' }}</span>
              </button>
              <button type="button" class="btn btn-secondary" @click="resetForm">
                重置
              </button>
            </div>
          </form>
        </div>
      </div>

      <!-- 密码修改卡片 -->
      <div class="password-card glass-card">
        <h3 class="card-title">
          <svg class="title-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          修改密码
        </h3>
        
        <form @submit.prevent="changePassword">
          <div class="form-group">
            <label class="form-label">当前密码</label>
            <div class="input-wrapper">
              <input 
                v-model="passwordForm.currentPassword" 
                :type="showCurrentPassword ? 'text' : 'password'"
                class="form-input"
                placeholder="请输入当前密码"
                required
              >
              <button type="button" class="password-toggle" @click="showCurrentPassword = !showCurrentPassword">
                <svg v-if="showCurrentPassword" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <svg v-else viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M3.98 8.223A10.477 10.477 0 001.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.45 10.45 0 0112 4.5c4.756 0 8.773 3.162 10.065 7.498a10.523 10.523 0 01-4.293 5.774M6.228 6.228L3 3m3.228 3.228l3.65 3.65m7.894 7.894L21 21m-3.228-3.228l-3.65-3.65m0 0a3 3 0 10-4.243-4.243m4.242 4.242L9.88 9.88" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
            </div>
          </div>

          <div class="form-group">
            <label class="form-label">新密码</label>
            <div class="input-wrapper">
              <input 
                v-model="passwordForm.newPassword" 
                :type="showNewPassword ? 'text' : 'password'"
                class="form-input"
                placeholder="请输入新密码"
                required
              >
              <button type="button" class="password-toggle" @click="showNewPassword = !showNewPassword">
                <svg v-if="showNewPassword" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <svg v-else viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M3.98 8.223A10.477 10.477 0 001.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.45 10.45 0 0112 4.5c4.756 0 8.773 3.162 10.065 7.498a10.523 10.523 0 01-4.293 5.774M6.228 6.228L3 3m3.228 3.228l3.65 3.65m7.894 7.894L21 21m-3.228-3.228l-3.65-3.65m0 0a3 3 0 10-4.243-4.243m4.242 4.242L9.88 9.88" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
            </div>
            <div class="password-strength">
              <div class="strength-bar">
                <div class="strength-fill" :class="passwordStrength.class" :style="{ width: passwordStrength.width }"></div>
              </div>
              <span class="strength-text">{{ passwordStrength.text }}</span>
            </div>
          </div>

          <div class="form-group">
            <label class="form-label">确认新密码</label>
            <div class="input-wrapper">
              <input 
                v-model="passwordForm.confirmPassword" 
                :type="showConfirmPassword ? 'text' : 'password'"
                class="form-input"
                placeholder="请再次输入新密码"
                required
              >
              <button type="button" class="password-toggle" @click="showConfirmPassword = !showConfirmPassword">
                <svg v-if="showConfirmPassword" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <svg v-else viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M3.98 8.223A10.477 10.477 0 001.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.45 10.45 0 0112 4.5c4.756 0 8.773 3.162 10.065 7.498a10.523 10.523 0 01-4.293 5.774M6.228 6.228L3 3m3.228 3.228l3.65 3.65m7.894 7.894L21 21m-3.228-3.228l-3.65-3.65m0 0a3 3 0 10-4.243-4.243m4.242 4.242L9.88 9.88" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
            </div>
          </div>

          <div class="form-actions">
            <button type="submit" class="btn btn-primary" :disabled="passwordLoading || !isPasswordValid">
              <span v-if="passwordLoading" class="loading-spinner"></span>
              <span>{{ passwordLoading ? '修改中...' : '修改密码' }}</span>
            </button>
          </div>
        </form>
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
import { ref, reactive, computed, onMounted } from 'vue'
import { useUserStore } from '../store'
import { useRouter } from 'vue-router'

const userStore = useUserStore()
const router = useRouter()
const loading = ref(false)
const passwordLoading = ref(false)
const avatarInput = ref(null)

// 密码显示状态
const showCurrentPassword = ref(false)
const showNewPassword = ref(false)
const showConfirmPassword = ref(false)

// 状态提示
const alert = reactive({
  show: false,
  type: 'info',
  message: ''
})

// 用户资料
const userProfile = computed(() => userStore.getUser || {
  username: 'admin',
  email: 'user@example.com',
  role: 'admin',
  realName: '',
  phone: '',
  department: '',
  position: '',
  bio: ''
})

// 个人资料表单
const profileForm = reactive({
  username: '',
  email: '',
  realName: '',
  phone: '',
  department: '',
  position: '',
  bio: ''
})

// 密码修改表单
const passwordForm = reactive({
  currentPassword: '',
  newPassword: '',
  confirmPassword: ''
})

// 用户头像颜色
const avatarColor = computed(() => {
  const colors = ['#4facfe', '#00f2fe', '#43e97b', '#38f9d7', '#667eea', '#764ba2']
  const index = userProfile.value.username ? userProfile.value.username.charCodeAt(0) % colors.length : 0
  return colors[index]
})

// 用户名首字母
const userInitial = computed(() => {
  return userProfile.value.username ? userProfile.value.username.charAt(0).toUpperCase() : 'U'
})

// 密码强度检测
const passwordStrength = computed(() => {
  const password = passwordForm.newPassword
  if (!password) return { width: '0%', class: '', text: '' }

  let score = 0
  if (password.length >= 8) score++
  if (/[a-z]/.test(password)) score++
  if (/[A-Z]/.test(password)) score++
  if (/[0-9]/.test(password)) score++
  if (/[^A-Za-z0-9]/.test(password)) score++

  if (score <= 2) return { width: '33%', class: 'weak', text: '弱' }
  if (score <= 3) return { width: '66%', class: 'medium', text: '中等' }
  return { width: '100%', class: 'strong', text: '强' }
})

// 密码验证
const isPasswordValid = computed(() => {
  return passwordForm.newPassword &&
         passwordForm.confirmPassword &&
         passwordForm.newPassword === passwordForm.confirmPassword &&
         passwordForm.newPassword.length >= 6
})

// 初始化表单数据
const initializeForm = () => {
  Object.assign(profileForm, {
    username: userProfile.value.username || '',
    email: userProfile.value.email || '',
    realName: userProfile.value.realName || '',
    phone: userProfile.value.phone || '',
    department: userProfile.value.department || '',
    position: userProfile.value.position || '',
    bio: userProfile.value.bio || ''
  })
}

// 显示提示消息
const showAlert = (type, message) => {
  alert.show = true
  alert.type = type
  alert.message = message

  setTimeout(() => {
    alert.show = false
  }, 3000)
}

// 更新个人资料
const updateProfile = async () => {
  loading.value = true
  try {
    // 这里应该调用API更新用户资料
    await new Promise(resolve => setTimeout(resolve, 1000)) // 模拟API调用

    // 更新用户存储中的信息
    userStore.updateUserProfile(profileForm)

    showAlert('success', '个人资料更新成功！')
  } catch (error) {
    console.error('更新个人资料失败:', error)
    showAlert('error', '更新失败，请稍后重试')
  } finally {
    loading.value = false
  }
}

// 重置表单
const resetForm = () => {
  initializeForm()
  showAlert('info', '表单已重置')
}

// 修改密码
const changePassword = async () => {
  if (!isPasswordValid.value) {
    showAlert('error', '请检查密码输入')
    return
  }

  passwordLoading.value = true
  try {
    // 这里应该调用API修改密码
    await new Promise(resolve => setTimeout(resolve, 1000)) // 模拟API调用

    // 清空密码表单
    Object.assign(passwordForm, {
      currentPassword: '',
      newPassword: '',
      confirmPassword: ''
    })

    showAlert('success', '密码修改成功！')
  } catch (error) {
    console.error('修改密码失败:', error)
    showAlert('error', '密码修改失败，请稍后重试')
  } finally {
    passwordLoading.value = false
  }
}

// 触发头像上传
const triggerAvatarUpload = () => {
  avatarInput.value?.click()
}

// 处理头像上传
const handleAvatarChange = (event) => {
  const file = event.target.files[0]
  if (file) {
    // 这里应该上传头像到服务器
    console.log('上传头像:', file)
    showAlert('info', '头像上传功能开发中...')
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

// 组件挂载时初始化
onMounted(() => {
  initializeForm()
})
</script>

<style scoped>
.profile-container {
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

/* 主要内容 */
.profile-content {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: var(--spacing-2xl);
}

/* 个人资料卡片 */
.profile-card {
  padding: var(--spacing-2xl);
}

.profile-header {
  display: flex;
  align-items: center;
  gap: var(--spacing-xl);
  margin-bottom: var(--spacing-2xl);
  padding-bottom: var(--spacing-xl);
  border-bottom: 1px solid var(--border-color);
}

.avatar-section {
  position: relative;
}

.avatar-container {
  position: relative;
  display: inline-block;
}

.user-avatar {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
  font-weight: 700;
  color: white;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  box-shadow: var(--shadow-lg);
}

.avatar-upload-btn {
  position: absolute;
  bottom: 8px;
  right: 8px;
  width: 36px;
  height: 36px;
  background: var(--primary-color);
  border: none;
  border-radius: 50%;
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: var(--shadow-md);
  transition: var(--transition-normal);
}

.avatar-upload-btn:hover {
  background: var(--primary-dark);
  transform: scale(1.1);
}

.avatar-upload-btn svg {
  width: 18px;
  height: 18px;
}

.user-info {
  flex: 1;
}

.user-name {
  font-size: 1.8rem;
  font-weight: 700;
  color: #ffffff;
  margin: 0 0 var(--spacing-sm) 0;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
  letter-spacing: -0.01em;
}

.user-role {
  display: inline-block;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  color: white;
  padding: var(--spacing-xs) var(--spacing-md);
  border-radius: var(--radius-full);
  font-size: 0.9rem;
  font-weight: 600;
  margin-bottom: var(--spacing-sm);
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
  box-shadow: 0 2px 8px rgba(79, 172, 254, 0.3);
}

.user-email {
  font-size: 1rem;
  color: rgba(255, 255, 255, 0.9);
  margin: 0;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

/* 表单样式 */
.profile-form {
  margin-top: var(--spacing-xl);
}

.form-title {
  font-size: 1.3rem;
  font-weight: 600;
  color: #ffffff;
  margin: 0 0 var(--spacing-xl) 0;
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5);
  letter-spacing: -0.01em;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--spacing-lg);
  margin-bottom: var(--spacing-lg);
}

.form-group {
  margin-bottom: var(--spacing-lg);
}

.form-label {
  display: block;
  margin-bottom: var(--spacing-sm);
  font-size: 1rem;
  font-weight: 600;
  color: #ffffff;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5);
  letter-spacing: 0.02em;
}

.form-input, .form-select, .form-textarea {
  width: 100%;
  padding: var(--spacing-md);
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: var(--radius-md);
  color: #ffffff !important;
  font-size: 1rem;
  font-weight: 500;
  transition: var(--transition-normal);
  font-family: inherit;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

/* 特别针对select元素的样式 */
.form-select {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6,9 12,15 18,9'%3e%3c/polyline%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right 12px center;
  background-size: 16px;
  padding-right: 40px;
}

.form-input::placeholder, .form-textarea::placeholder {
  color: rgba(255, 255, 255, 0.5);
  font-weight: 400;
  text-shadow: none;
}

.form-input:focus, .form-select:focus, .form-textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(79, 172, 254, 0.2);
  background: rgba(255, 255, 255, 0.12);
  color: #ffffff;
}

/* 下拉框选项样式 */
.form-select option {
  background: #1e293b;
  color: #ffffff;
  padding: var(--spacing-sm);
  font-weight: 500;
  border: none;
}

.form-select option:hover {
  background: #334155;
}

.form-select option:checked {
  background: var(--primary-color);
  color: #ffffff;
}

.form-textarea {
  resize: vertical;
  min-height: 100px;
}

.form-actions {
  display: flex;
  gap: var(--spacing-md);
  margin-top: var(--spacing-xl);
}

/* 按钮样式 */
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

/* 密码卡片 */
.password-card {
  padding: var(--spacing-2xl);
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
}

/* 密码输入框 */
.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
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
}

.password-toggle:hover {
  color: var(--primary-color);
  background: rgba(79, 172, 254, 0.1);
}

.password-toggle svg {
  width: 18px;
  height: 18px;
}

/* 密码强度指示器 */
.password-strength {
  margin-top: var(--spacing-sm);
}

.strength-bar {
  width: 100%;
  height: 4px;
  background: var(--bg-secondary);
  border-radius: var(--radius-sm);
  overflow: hidden;
  margin-bottom: var(--spacing-xs);
}

.strength-fill {
  height: 100%;
  transition: var(--transition-normal);
  border-radius: var(--radius-sm);
}

.strength-fill.weak {
  background: var(--error-color);
}

.strength-fill.medium {
  background: var(--warning-color);
}

.strength-fill.strong {
  background: var(--success-color);
}

.strength-text {
  font-size: 0.8rem;
  color: var(--text-muted);
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

/* 玻璃态卡片 */
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
  .profile-content {
    grid-template-columns: 1fr;
    gap: var(--spacing-xl);
  }
}

@media (max-width: 768px) {
  .profile-container {
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

  .profile-header {
    flex-direction: column;
    text-align: center;
    gap: var(--spacing-lg);
  }

  .form-row {
    grid-template-columns: 1fr;
    gap: 0;
  }

  .user-avatar {
    width: 100px;
    height: 100px;
    font-size: 2.5rem;
  }

  .form-actions {
    flex-direction: column;
  }
}

@media (max-width: 480px) {
  .profile-container {
    padding: var(--spacing-md);
  }

  .profile-card, .password-card {
    padding: var(--spacing-lg);
  }

  .page-title {
    font-size: 1.5rem;
  }

  .user-name {
    font-size: 1.5rem;
  }
}
</style>
