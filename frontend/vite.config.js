import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  plugins: [
    vue({
      template: {
        compilerOptions: {
          // 更全面地处理自定义元素，包括Element Plus组件和Web Components
          isCustomElement: (tag) => {
            return tag.startsWith('el-') || 
                  ['el-icon', 'el-button', 'el-card'].includes(tag)
          },
          // 禁用模板中的某些警告
          whitespace: 'preserve',
          // 添加额外的转换
          nodeTransforms: []
        }
      }
    })
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    }
  },
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
        secure: false
      }
    }
  },
  build: {
    rollupOptions: {
      input: {
        main: path.resolve(__dirname, 'index.html')
      }
    }
  },
  optimizeDeps: {
    include: ['vue', 'vue-router', 'pinia', 'axios', 'echarts', 'element-plus', '@element-plus/icons-vue']
  }
}) 