export default {
  // 通用
  common: {
    appName: '数据分析平台',
    confirm: '确认',
    cancel: '取消',
    save: '保存',
    delete: '删除',
    edit: '编辑',
    add: '添加',
    search: '搜索',
    loading: '加载中...',
    success: '成功',
    error: '错误',
    warning: '警告',
    info: '信息',
    close: '关闭',
    back: '返回',
    next: '下一步',
    previous: '上一步',
    submit: '提交',
    reset: '重置',
    refresh: '刷新',
    export: '导出',
    import: '导入',
    download: '下载',
    upload: '上传',
    view: '查看',
    more: '更多'
  },

  // 导航
  nav: {
    home: '首页',
    dashboard: '数据仪表盘',
    analysis: '数据分析',
    reports: '报表管理',
    dataScreen: '数字大屏',
    dataWarehouse: '数字大厦',
    settings: '设置',
    profile: '个人资料',
    logout: '退出登录'
  },

  // 首页
  home: {
    title: '数据分析平台',
    subtitle: '智能 · 高效 · 专业',
    description: '基于先进算法的企业级数据分析解决方案\n让数据驱动您的每一个决策',
    getStarted: '立即开始',
    learnMore: '了解更多',
    features: {
      title: '核心功能',
      subtitle: '强大的数据处理能力，满足您的各种分析需求',
      dashboard: {
        title: '数据仪表盘',
        description: '实时监控关键业务指标，通过直观的图表和数据可视化，让您快速掌握业务全貌'
      },
      analysis: {
        title: '多维分析',
        description: '从多个角度探索数据规律，发现隐藏的商业洞察，为决策提供科学依据'
      },
      reports: {
        title: '报表生成',
        description: '自动创建专业报表，支持多种格式导出，让数据展示更加直观和专业'
      },
      prediction: {
        title: '预测分析',
        description: '利用机器学习算法预测业务趋势，提前识别机会和风险'
      }
    },
    stats: {
      users: '企业用户',
      stability: '系统稳定性',
      support: '技术支持'
    }
  },

  // 登录
  login: {
    title: '登录',
    subtitle: '欢迎回来',
    username: '用户名',
    password: '密码',
    rememberMe: '记住我',
    forgotPassword: '忘记密码？',
    loginButton: '登录',
    noAccount: '还没有账户？',
    register: '立即注册',
    loginSuccess: '登录成功',
    loginFailed: '登录失败',
    invalidCredentials: '用户名或密码错误',
    placeholder: {
      username: '请输入用户名',
      password: '请输入密码'
    }
  },

  // 设置
  settings: {
    title: '系统设置',
    subtitle: '个性化您的使用体验',
    appearance: {
      title: '外观设置',
      theme: {
        label: '主题模式',
        description: '选择您喜欢的界面主题',
        dark: '深色',
        light: '浅色',
        auto: '自动'
      },
      language: {
        label: '界面语言',
        description: '选择界面显示语言'
      },
      animations: {
        label: '动画效果',
        description: '启用或禁用界面动画'
      }
    },
    data: {
      title: '数据设置',
      autoRefresh: {
        label: '自动刷新',
        description: '自动刷新数据的时间间隔',
        options: {
          off: '关闭',
          '30s': '30秒',
          '1m': '1分钟',
          '5m': '5分钟',
          '10m': '10分钟'
        }
      },
      cache: {
        label: '数据缓存',
        description: '启用数据缓存以提高性能'
      },
      realTime: {
        label: '实时数据',
        description: '启用实时数据推送'
      }
    },
    notifications: {
      title: '通知设置',
      desktop: {
        label: '桌面通知',
        description: '允许显示桌面通知'
      },
      email: {
        label: '邮件通知',
        description: '接收重要事件的邮件通知'
      },
      sound: {
        label: '声音提示',
        description: '播放通知声音'
      }
    },
    security: {
      title: '安全设置',
      autoLogout: {
        label: '自动登出',
        description: '无操作时自动登出的时间',
        options: {
          never: '从不',
          '15m': '15分钟',
          '30m': '30分钟',
          '1h': '1小时',
          '2h': '2小时'
        }
      },
      twoFactor: {
        label: '双因素认证',
        description: '启用双因素身份验证'
      },
      loginHistory: {
        label: '登录历史',
        description: '记录登录历史记录'
      }
    },
    actions: {
      save: '保存设置',
      saving: '保存中...',
      reset: '重置为默认',
      clearCache: '清除缓存'
    },
    messages: {
      updated: '设置已更新',
      saved: '设置保存成功！',
      resetSuccess: '设置已重置为默认值',
      cacheCleared: '缓存清除成功！',
      updateFailed: '更新设置失败',
      saveFailed: '保存失败，请稍后重试',
      resetFailed: '重置设置失败',
      cacheClearFailed: '清除缓存失败',
      loadFailed: '加载设置失败'
    }
  },

  // 搜索
  search: {
    placeholder: '搜索报表、分析、用户...',
    noResults: '没有找到相关结果',
    suggestions: '搜索建议',
    recent: '最近搜索',
    clear: '清除搜索'
  },

  // 用户菜单
  user: {
    defaultName: '用户',
    profile: '个人资料',
    settings: '设置',
    help: '帮助',
    logout: '退出登录',
    role: {
      admin: '管理员',
      user: '普通用户',
      guest: '访客'
    }
  },

  // 错误信息
  errors: {
    networkError: '网络连接错误',
    serverError: '服务器错误',
    notFound: '页面未找到',
    unauthorized: '未授权访问',
    forbidden: '访问被禁止',
    timeout: '请求超时',
    unknown: '未知错误'
  }
}
