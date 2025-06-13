import { defineStore } from 'pinia'
import axios from 'axios'
import CryptoJS from 'crypto-js'

// 安全密钥，实际应用中应从环境变量获取
const SECURITY_KEY = 'data-analysis-platform-secret-key-2023'

// 加密密码函数
const encryptPassword = (password) => {
  // 使用SHA256进行密码哈希
  return CryptoJS.SHA256(password).toString(CryptoJS.enc.Hex)
}

// 模拟数据
const mockData = {
  dashboardData: {
    metrics: [
      { title: '总销售额', value: '¥120,000', change: 12.5 },
      { title: '新增用户', value: '1,520', change: 3.8 },
      { title: '订单数量', value: '2,450', change: -2.3 },
      { title: '客单价', value: '¥48.9', change: 8.2 }
    ],
    salesTrend: [30000, 28000, 36000, 42000, 45000, 50000, 60000],
    userDistribution: [
      { value: 1048, name: '华东' },
      { value: 735, name: '华南' },
      { value: 580, name: '华北' },
      { value: 484, name: '西南' },
      { value: 300, name: '西北' }
    ],
    productSales: {
      lastYear: [320, 302, 301, 334, 390],
      currentYear: [420, 382, 391, 434, 490]
    }
  },
  analysisData: {
    trends: [
      { date: '2023-01', value: 105 },
      { date: '2023-02', value: 120 },
      { date: '2023-03', value: 135 },
      { date: '2023-04', value: 125 },
      { date: '2023-05', value: 160 },
      { date: '2023-06', value: 190 }
    ],
    categories: [
      { name: '电子产品', value: 42 },
      { name: '服装', value: 28 },
      { name: '食品', value: 15 },
      { name: '家居', value: 10 },
      { name: '其他', value: 5 }
    ]
  },
  reports: [
    { id: 1, title: '2023年第一季度销售报告', date: '2023-04-01', status: 'completed' },
    { id: 2, title: '用户增长分析', date: '2023-04-15', status: 'completed' },
    { id: 3, title: '产品性能评估', date: '2023-05-01', status: 'in-progress' },
    { id: 4, title: '市场竞争分析', date: '2023-05-10', status: 'pending' }
  ]
}

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null,
    isAuthenticated: localStorage.getItem('token') ? true : false, // 根据token初始化登录状态
    token: localStorage.getItem('token') || null,
    useMockData: false // 默认不使用模拟数据模式，使用真实后端
  }),
  getters: {
    getUser: (state) => state.user,
    isLoggedIn: (state) => state.isAuthenticated
  },
  actions: {
    async login(credentials) {
      try {
        if (this.useMockData) {
          // 使用模拟数据时，模拟成功登录
          console.log('使用模拟数据进行登录')
          
          // 模拟的token和用户数据
          const mockToken = 'mock-jwt-token-' + Date.now();
          const mockUser = {
            username: credentials.username,
            role: credentials.username === 'admin' ? 'admin' : 'user'
          };
          
          // 更新状态
          this.token = mockToken;
          this.user = mockUser;
          this.isAuthenticated = true;
          localStorage.setItem('token', mockToken);
          
          return Promise.resolve(mockUser);
        } else {
          // 尝试真实登录，对密码进行加密处理
          console.log('发送真实登录请求到后端')
          
          // 创建一个新的凭据对象，包含加密后的密码
          const secureCredentials = {
            username: credentials.username,
            password: encryptPassword(credentials.password),
            clientTimestamp: Date.now() // 添加时间戳防止重放攻击
          }
          
          const response = await axios.post('/auth/login', secureCredentials)
          console.log('登录响应:', response.data)
          
          const { token, user } = response.data
          
          this.token = token
          this.user = user
          this.isAuthenticated = true
          localStorage.setItem('token', token)
          
          return Promise.resolve(user)
        }
      } catch (error) {
        console.error('登录失败:', error)
        return Promise.reject(error)
      }
    },
    logout() {
      this.user = null
      this.token = null
      this.isAuthenticated = false
      localStorage.removeItem('token')
    },
    
    // 切换是否使用模拟数据
    toggleMockData(value) {
      this.useMockData = value !== undefined ? value : !this.useMockData
    },

    // 更新用户资料
    updateUserProfile(profileData) {
      if (this.user) {
        this.user = { ...this.user, ...profileData }
        // 这里应该调用API更新用户资料
        console.log('更新用户资料:', this.user)
      }
    },

    // 获取用户资料
    async fetchUserProfile() {
      try {
        if (this.useMockData) {
          // 使用模拟数据
          const mockProfile = {
            username: this.user?.username || 'admin',
            email: 'user@example.com',
            realName: '管理员',
            phone: '138****8888',
            department: '技术部',
            position: '系统管理员',
            bio: '负责系统维护和用户管理',
            role: this.user?.role || 'admin'
          }
          this.user = { ...this.user, ...mockProfile }
          return Promise.resolve(mockProfile)
        } else {
          // 调用真实API
          const response = await axios.get('/user/profile')
          const profile = response.data
          this.user = { ...this.user, ...profile }
          return Promise.resolve(profile)
        }
      } catch (error) {
        console.error('获取用户资料失败:', error)
        return Promise.reject(error)
      }
    }
  }
})

// 设置状态管理
export const useSettingsStore = defineStore('settings', {
  state: () => ({
    theme: 'dark',
    language: 'zh-CN',
    animations: true,
    autoRefresh: 60,
    dataCache: true,
    realTimeData: true,
    desktopNotifications: true,
    emailNotifications: false,
    soundNotifications: true,
    autoLogout: 30,
    twoFactorAuth: false,
    loginHistory: true,
    loading: false
  }),
  getters: {
    getTheme: (state) => state.theme,
    getLanguage: (state) => state.language,
    getAllSettings: (state) => {
      const { loading, ...settings } = state
      return settings
    }
  },
  actions: {
    // 加载设置
    async loadSettings() {
      try {
        console.log('开始加载设置...')

        // 首先从localStorage加载
        const savedSettings = localStorage.getItem('userSettings')
        if (savedSettings) {
          try {
            const settings = JSON.parse(savedSettings)
            console.log('从localStorage加载的设置:', settings)

            // 只更新存在的设置项，保持默认值
            Object.keys(settings).forEach(key => {
              if (this.hasOwnProperty(key) && key !== 'loading') {
                this[key] = settings[key]
              }
            })
          } catch (error) {
            console.error('解析localStorage设置失败:', error)
          }
        }

        // 如果用户已登录，尝试从服务器加载
        const userStore = useUserStore()
        if (userStore.isAuthenticated) {
          try {
            const response = await axios.get('/user/settings')
            console.log('从服务器加载的设置:', response.data)

            // 更新设置
            Object.keys(response.data).forEach(key => {
              if (this.hasOwnProperty(key) && key !== 'loading') {
                this[key] = response.data[key]
              }
            })

            // 同步到localStorage
            localStorage.setItem('userSettings', JSON.stringify(this.getAllSettings))
          } catch (error) {
            console.warn('无法从服务器加载设置，使用本地设置:', error)
          }
        }

        console.log('最终设置状态:', this.getAllSettings)

        // 应用主题
        this.applyTheme()
      } catch (error) {
        console.error('加载设置失败:', error)
        // 确保至少应用默认主题
        this.applyTheme()
      }
    },

    // 更新单个设置
    async updateSetting(key, value) {
      console.log(`更新设置: ${key} = ${value}`)

      // 更新状态
      this[key] = value

      // 立即保存到localStorage
      const settingsToSave = this.getAllSettings
      localStorage.setItem('userSettings', JSON.stringify(settingsToSave))
      console.log('保存到localStorage:', settingsToSave)

      // 应用特定设置
      if (key === 'theme') {
        console.log('应用主题变更:', value)
        this.applyTheme()
      } else if (key === 'language') {
        console.log('应用语言变更:', value)
        this.applyLanguage(value)
      }

      // 如果用户已登录，同步到服务器
      const userStore = useUserStore()
      if (userStore.isAuthenticated) {
        try {
          await axios.put('/user/settings', { [key]: value })
          console.log('设置已同步到服务器')
        } catch (error) {
          console.warn('无法同步设置到服务器:', error)
        }
      }
    },

    // 保存所有设置
    async saveSettings() {
      this.loading = true
      try {
        // 保存到localStorage
        localStorage.setItem('userSettings', JSON.stringify(this.getAllSettings))

        // 如果用户已登录，保存到服务器
        const userStore = useUserStore()
        if (userStore.isAuthenticated) {
          await axios.put('/user/settings', this.getAllSettings)
        }

        // 应用所有设置
        this.applyTheme()

        return Promise.resolve()
      } catch (error) {
        console.error('保存设置失败:', error)
        return Promise.reject(error)
      } finally {
        this.loading = false
      }
    },

    // 重置设置
    resetSettings() {
      Object.assign(this, {
        theme: 'dark',
        language: 'zh-CN',
        animations: true,
        autoRefresh: 60,
        dataCache: true,
        realTimeData: true,
        desktopNotifications: true,
        emailNotifications: false,
        soundNotifications: true,
        autoLogout: 30,
        twoFactorAuth: false,
        loginHistory: true
      })

      // 保存重置后的设置
      this.saveSettings()
    },

    // 应用主题
    applyTheme() {
      const root = document.documentElement

      // 移除所有主题类
      root.classList.remove('light-theme', 'dark-theme')

      if (this.theme === 'light') {
        root.classList.add('light-theme')
        console.log('应用浅色主题')
      } else if (this.theme === 'dark') {
        root.classList.add('dark-theme')
        console.log('应用深色主题')
      } else if (this.theme === 'auto') {
        // 自动主题：根据系统偏好设置
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches
        const appliedTheme = prefersDark ? 'dark-theme' : 'light-theme'
        root.classList.add(appliedTheme)
        console.log('应用自动主题:', appliedTheme)
      }

      // 强制重新渲染样式
      root.style.display = 'none'
      root.offsetHeight // 触发重排
      root.style.display = ''
    },

    // 应用语言
    applyLanguage(locale) {
      try {
        // 动态导入i18n模块
        import('../i18n/index.js').then(({ setLanguage }) => {
          const success = setLanguage(locale)
          if (success) {
            console.log('语言已应用:', locale)
            // 更新HTML lang属性
            document.documentElement.lang = locale
          } else {
            console.error('不支持的语言:', locale)
          }
        }).catch(error => {
          console.error('加载i18n模块失败:', error)
        })
      } catch (error) {
        console.error('应用语言失败:', error)
      }
    }
  }
})

export const useDataStore = defineStore('data', {
  state: () => ({
    dashboardData: null,
    analysisData: null,
    reports: [],
    loading: false
  }),
  getters: {
    getDashboardData: (state) => state.dashboardData,
    getAnalysisData: (state) => state.analysisData,
    getReports: (state) => state.reports
  },
  actions: {
    async fetchDashboardData() {
      this.loading = true
      try {
        const userStore = useUserStore();
        if (userStore.useMockData) {
          // 使用模拟数据
          console.log('使用仪表盘模拟数据（后端不可用）')
          this.dashboardData = mockData.dashboardData
          this.loading = false
          return Promise.resolve(mockData.dashboardData)
        } else {
          const response = await axios.get('/dashboard')
          this.dashboardData = response.data
          this.loading = false
          return Promise.resolve(response.data)
        }
      } catch (error) {
        console.warn('无法连接到后端，使用模拟数据', error)
        this.dashboardData = mockData.dashboardData
        this.loading = false
        return Promise.resolve(mockData.dashboardData)
      }
    },
    async fetchAnalysisData(params) {
      this.loading = true
      try {
        const userStore = useUserStore();
        if (userStore.useMockData) {
          // 使用模拟数据
          console.log('使用分析模拟数据（后端不可用）')
          this.analysisData = mockData.analysisData
          this.loading = false
          return Promise.resolve(mockData.analysisData)
        } else {
          const response = await axios.get('/analysis', { params })
          this.analysisData = response.data
          this.loading = false
          return Promise.resolve(response.data)
        }
      } catch (error) {
        console.warn('无法连接到后端，使用模拟数据', error)
        this.analysisData = mockData.analysisData
        this.loading = false
        return Promise.resolve(mockData.analysisData)
      }
    },
    async fetchReports() {
      this.loading = true
      try {
        const userStore = useUserStore();
        if (userStore.useMockData) {
          // 使用模拟数据
          console.log('使用报告模拟数据（后端不可用）')
          this.reports = mockData.reports
          this.loading = false
          return Promise.resolve(mockData.reports)
        } else {
          const response = await axios.get('/reports')
          this.reports = response.data
          this.loading = false
          return Promise.resolve(response.data)
        }
      } catch (error) {
        console.warn('无法连接到后端，使用模拟数据', error)
        this.reports = mockData.reports
        this.loading = false
        return Promise.resolve(mockData.reports)
      }
    },
    // 不再需要toggleMockData方法，已移至userStore
  }
}) 