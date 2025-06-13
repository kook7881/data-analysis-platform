import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import './assets/main.css'
import './assets/components.css'
import './assets/reports.css'
import './assets/modal.css'
import './assets/search.css'
import './assets/notifications.css'
import axios from 'axios'
import i18n from './i18n'

// 配置axios默认设置
axios.defaults.timeout = 10000 // 10秒超时
axios.defaults.baseURL = '/api'    // 使用相对路径，通过Vite代理转发

// 添加请求拦截器，自动添加认证token
axios.interceptors.request.use(
  config => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  error => {
    return Promise.reject(error)
  }
)

const app = createApp(App)
const pinia = createPinia()

// 注册所有图标
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

app.use(router)
app.use(pinia)
app.use(i18n)
app.use(ElementPlus, { size: 'default' })

// 在应用挂载前初始化主题
function initializeTheme() {
  // 从localStorage读取保存的主题设置
  const savedSettings = localStorage.getItem('userSettings')
  let theme = 'dark' // 默认主题

  if (savedSettings) {
    try {
      const settings = JSON.parse(savedSettings)
      theme = settings.theme || 'dark'
    } catch (error) {
      console.warn('解析保存的设置失败:', error)
    }
  }

  // 立即应用主题类到document.documentElement
  const root = document.documentElement
  root.classList.remove('light-theme', 'dark-theme')

  if (theme === 'light') {
    root.classList.add('light-theme')
  } else if (theme === 'dark') {
    root.classList.add('dark-theme')
  } else if (theme === 'auto') {
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches
    root.classList.add(prefersDark ? 'dark-theme' : 'light-theme')
  }

  console.log('初始化主题:', theme, '应用的类:', root.className)
}

// 初始化主题
initializeTheme()

app.mount('#app')