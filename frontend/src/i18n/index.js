import { createI18n } from 'vue-i18n'
import zhCN from '../locales/zh-CN.js'
import enUS from '../locales/en-US.js'
import jaJP from '../locales/ja-JP.js'

// 获取保存的语言设置
function getStoredLanguage() {
  try {
    const savedSettings = localStorage.getItem('userSettings')
    if (savedSettings) {
      const settings = JSON.parse(savedSettings)
      return settings.language || 'zh-CN'
    }
  } catch (error) {
    console.warn('Failed to parse stored language settings:', error)
  }
  return 'zh-CN' // 默认语言
}

// 语言配置
const messages = {
  'zh-CN': zhCN,
  'en-US': enUS,
  'ja-JP': jaJP
}

// 创建i18n实例
const i18n = createI18n({
  legacy: false, // 使用Composition API模式
  locale: getStoredLanguage(), // 设置默认语言
  fallbackLocale: 'zh-CN', // 设置备用语言
  messages,
  globalInjection: true, // 全局注入$t函数
  silentTranslationWarn: true, // 静默翻译警告
  silentFallbackWarn: true // 静默回退警告
})

// 切换语言的函数
export function setLanguage(locale) {
  if (messages[locale]) {
    i18n.global.locale.value = locale
    
    // 保存到localStorage
    try {
      const savedSettings = localStorage.getItem('userSettings')
      let settings = {}
      if (savedSettings) {
        settings = JSON.parse(savedSettings)
      }
      settings.language = locale
      localStorage.setItem('userSettings', JSON.stringify(settings))
      console.log('Language changed to:', locale)
    } catch (error) {
      console.error('Failed to save language setting:', error)
    }
    
    return true
  }
  return false
}

// 获取当前语言
export function getCurrentLanguage() {
  return i18n.global.locale.value
}

// 获取支持的语言列表
export function getSupportedLanguages() {
  return [
    { code: 'zh-CN', name: '简体中文', nativeName: '简体中文' },
    { code: 'en-US', name: 'English', nativeName: 'English' },
    { code: 'ja-JP', name: 'Japanese', nativeName: '日本語' }
  ]
}

// 检查是否支持某种语言
export function isLanguageSupported(locale) {
  return Object.keys(messages).includes(locale)
}

export default i18n
