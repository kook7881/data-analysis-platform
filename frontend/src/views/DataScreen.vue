<template>
  <div class="data-screen">
    <!-- 顶部标题栏 -->
    <header class="screen-header">
      <div class="header-left">
        <h1 class="screen-title">
          <span class="title-icon">📊</span>
          数据可视化大屏
        </h1>
        <p class="screen-subtitle">Data Visualization Dashboard</p>
      </div>
      <div class="header-right">
        <div class="time-display">
          <div class="current-time">{{ currentTime }}</div>
          <div class="current-date">{{ currentDate }}</div>
        </div>
        <div class="status-indicator">
          <div class="status-dot" :class="{ active: !isLoading }"></div>
          <span>{{ isLoading ? '数据更新中' : '实时监控' }}</span>
        </div>
      </div>
    </header>

    <!-- 主要内容区域 -->
    <main class="screen-main">
      <!-- 顶部统计卡片 -->
      <section class="stats-section">
        <div class="stats-grid">
          <div 
            v-for="(stat, index) in statsData" 
            :key="stat.id"
            class="stat-card"
            :style="{ animationDelay: index * 0.1 + 's' }"
          >
            <div class="stat-icon" :style="{ background: stat.color }">
              {{ stat.icon }}
            </div>
            <div class="stat-content">
              <div class="stat-label">{{ stat.label }}</div>
              <div class="stat-value">{{ stat.value }}</div>
              <div class="stat-change" :class="stat.trend >= 0 ? 'positive' : 'negative'">
                <span class="change-icon">{{ stat.trend >= 0 ? '↗' : '↘' }}</span>
                <span>{{ Math.abs(stat.trend) }}%</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 主要图表区域 -->
      <section class="charts-section">
        <div class="charts-grid">
          <!-- 左侧：销售趋势图 -->
          <div class="chart-card trend-chart">
            <div class="card-header">
              <h3>销售趋势</h3>
              <div class="time-filter">
                <button 
                  v-for="period in timePeriods" 
                  :key="period.value"
                  :class="{ active: selectedPeriod === period.value }"
                  @click="selectedPeriod = period.value"
                >
                  {{ period.label }}
                </button>
              </div>
            </div>
            <div ref="trendChartRef" class="chart-container"></div>
          </div>

          <!-- 中间：地图 -->
          <div class="chart-card map-chart">
            <div class="card-header">
              <h3>全国销售分布</h3>
              <div class="map-legend">
                <div v-for="item in mapLegend" :key="item.label" class="legend-item">
                  <div class="legend-color" :style="{ background: item.color }"></div>
                  <span>{{ item.label }}</span>
                </div>
              </div>
            </div>
            <div ref="mapChartRef" class="chart-container"></div>
          </div>

          <!-- 右侧：实时数据 -->
          <div class="chart-card realtime-data">
            <div class="card-header">
              <h3>实时交易</h3>
              <div class="live-indicator">
                <div class="live-dot"></div>
                <span>LIVE</span>
              </div>
            </div>
            <div class="realtime-container">
              <div class="realtime-list">
                <div
                  v-for="(item, index) in realtimeData"
                  :key="`realtime-${item.id}-${index}`"
                  class="realtime-item"
                >
                  <div class="item-avatar" :style="{ background: item.color }">
                    {{ item.region.charAt(0) }}
                  </div>
                  <div class="item-content">
                    <div class="item-region">{{ item.region }}</div>
                    <div class="item-amount">¥{{ item.amount.toLocaleString() }}</div>
                  </div>
                  <div class="item-time">{{ item.time }}</div>
                </div>
              </div>
              <div class="realtime-stats">
                <div class="stats-item">
                  <span class="stats-label">今日交易</span>
                  <span class="stats-value">{{ realtimeData.length * 127 }}</span>
                </div>
                <div class="stats-item">
                  <span class="stats-label">交易总额</span>
                  <span class="stats-value">¥{{ (realtimeData.reduce((sum, item) => sum + item.amount, 0) * 8.5).toLocaleString() }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 底部图表区域 -->
      <section class="bottom-section">
        <div class="bottom-grid">
          <!-- 产品销售排行 -->
          <div class="chart-card ranking-chart">
            <div class="card-header">
              <h3>产品销售排行</h3>
            </div>
            <div ref="rankingChartRef" class="chart-container"></div>
          </div>

          <!-- 地区销售对比 -->
          <div class="chart-card region-chart">
            <div class="card-header">
              <h3>地区销售对比</h3>
            </div>
            <div ref="regionChartRef" class="chart-container"></div>
          </div>

          <!-- 系统监控 -->
          <div class="chart-card monitor-panel">
            <div class="card-header">
              <h3>系统监控</h3>
            </div>
            <div class="monitor-content">
              <div v-for="metric in systemMetrics" :key="metric.name" class="monitor-item">
                <div class="metric-label">{{ metric.label }}</div>
                <div class="metric-value">{{ metric.value }}{{ metric.unit }}</div>
                <div class="metric-bar">
                  <div 
                    class="metric-progress" 
                    :style="{ 
                      width: metric.percentage + '%',
                      background: metric.color 
                    }"
                  ></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>

    <!-- 底部状态栏 -->
    <footer class="screen-footer">
      <div class="footer-left">
        <span>数据更新时间：{{ lastUpdateTime }}</span>
        <span>|</span>
        <span>在线用户：{{ onlineUsers }}</span>
      </div>
      <div class="footer-right">
        <span>© 2025 数据分析平台</span>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, onUnmounted, nextTick } from 'vue'
import * as echarts from 'echarts'
import axios from 'axios'

// 响应式数据
const currentTime = ref('')
const currentDate = ref('')
const isLoading = ref(false)
const lastUpdateTime = ref('')
const onlineUsers = ref(1247)
const selectedPeriod = ref('month')

// 时间周期选项
const timePeriods = [
  { label: '日', value: 'day' },
  { label: '周', value: 'week' },
  { label: '月', value: 'month' },
  { label: '年', value: 'year' }
]

// 统计数据
const statsData = reactive([
  {
    id: 1,
    label: '总销售额',
    value: '¥2,847.6万',
    trend: 12.5,
    icon: '💰',
    color: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
  },
  {
    id: 2,
    label: '订单数量',
    value: '18,694',
    trend: 8.3,
    icon: '📦',
    color: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)'
  },
  {
    id: 3,
    label: '活跃用户',
    value: '52,847',
    trend: 15.2,
    icon: '👥',
    color: 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)'
  },
  {
    id: 4,
    label: '转化率',
    value: '24.8%',
    trend: -2.1,
    icon: '📈',
    color: 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)'
  }
])

// 地图图例
const mapLegend = [
  { label: '500万+', color: '#ff4757' },
  { label: '300-500万', color: '#ff6b7a' },
  { label: '100-300万', color: '#ffa502' },
  { label: '50-100万', color: '#4a5568' },
  { label: '0-50万', color: '#1a202c' }
]

// 实时数据
const realtimeData = ref([])

// 系统监控指标
const systemMetrics = reactive([
  {
    name: 'cpu',
    label: 'CPU使用率',
    value: 45,
    unit: '%',
    percentage: 45,
    color: '#4facfe'
  },
  {
    name: 'memory',
    label: '内存使用率',
    value: 68,
    unit: '%',
    percentage: 68,
    color: '#f093fb'
  },
  {
    name: 'disk',
    label: '磁盘使用率',
    value: 32,
    unit: '%',
    percentage: 32,
    color: '#43e97b'
  },
  {
    name: 'network',
    label: '网络流量',
    value: 23.5,
    unit: 'MB/s',
    percentage: 75,
    color: '#ffa502'
  }
])

// 图表引用
const trendChartRef = ref(null)
const mapChartRef = ref(null)
const rankingChartRef = ref(null)
const regionChartRef = ref(null)

// 图表实例
let trendChart = null
let mapChart = null
let rankingChart = null
let regionChart = null

// 定时器
let timeTimer = null
let dataTimer = null

// API配置
const API_BASE_URL = 'http://localhost:5000/api'

// 更新时间
const updateTime = () => {
  const now = new Date()
  currentTime.value = now.toLocaleTimeString('zh-CN', { hour12: false })
  currentDate.value = now.toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    weekday: 'long'
  })
  lastUpdateTime.value = now.toLocaleTimeString('zh-CN', { hour12: false })
}

// 生成实时数据
let dataIdCounter = 0 // 添加计数器确保唯一ID

const generateRealtimeData = () => {
  const regions = ['北京', '上海', '广州', '深圳', '杭州', '南京', '成都', '武汉']
  const colors = ['#667eea', '#f093fb', '#4facfe', '#43e97b', '#ff6b7a', '#ffa502']

  // 使用计数器和时间戳确保唯一ID
  dataIdCounter++
  const newItem = {
    id: `${Date.now()}_${dataIdCounter}_${Math.random().toString(36).substr(2, 9)}`,
    region: regions[Math.floor(Math.random() * regions.length)],
    amount: Math.floor(Math.random() * 50000) + 10000,
    time: new Date().toLocaleTimeString('zh-CN', { hour12: false }),
    color: colors[Math.floor(Math.random() * colors.length)]
  }

  if (realtimeData.value.length >= 15) {
    realtimeData.value.pop()
  }
  realtimeData.value.unshift(newItem)

  // 确保没有重复的ID（额外保护）
  const uniqueData = []
  const seenIds = new Set()
  for (const item of realtimeData.value) {
    if (!seenIds.has(item.id)) {
      seenIds.add(item.id)
      uniqueData.push(item)
    }
  }
  realtimeData.value = uniqueData
}

// 更新系统监控数据
const updateSystemMetrics = () => {
  systemMetrics.forEach(metric => {
    const change = (Math.random() - 0.5) * 5 // 减小变化幅度
    metric.value = Math.max(0, Math.min(100, metric.value + change))

    if (metric.name === 'network') {
      metric.value = Math.round(metric.value * 10) / 10
      metric.percentage = Math.min(100, metric.value * 2) // 调整网络流量的百分比计算
    } else {
      metric.percentage = metric.value
      metric.value = Math.round(metric.value) // 确保整数显示
    }
  })
}

// 获取数据
const fetchData = async () => {
  try {
    isLoading.value = true
    const response = await axios.get(`${API_BASE_URL}/dataScreen`)

    if (response.data && response.data.metrics) {
      // 更新统计数据
      response.data.metrics.forEach((metric, index) => {
        if (statsData[index]) {
          statsData[index].value = metric.value
          statsData[index].trend = metric.change || 0
        }
      })
    }
  } catch (error) {
    console.log('使用模拟数据')
  } finally {
    isLoading.value = false
  }
}

// 初始化趋势图表
const initTrendChart = () => {
  if (!trendChartRef.value) return

  trendChart = echarts.init(trendChartRef.value)

  const option = {
    backgroundColor: 'transparent',
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      top: '10%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: ['1月', '2月', '3月', '4月', '5月', '6月'],
      axisLine: { lineStyle: { color: '#4a5568' } },
      axisLabel: { color: '#a0aec0' }
    },
    yAxis: {
      type: 'value',
      axisLine: { lineStyle: { color: '#4a5568' } },
      axisLabel: { color: '#a0aec0' },
      splitLine: { lineStyle: { color: '#2d3748' } }
    },
    series: [{
      data: [820, 932, 901, 934, 1290, 1330],
      type: 'line',
      smooth: true,
      lineStyle: { color: '#4facfe', width: 3 },
      itemStyle: { color: '#4facfe' },
      areaStyle: {
        color: {
          type: 'linear',
          x: 0, y: 0, x2: 0, y2: 1,
          colorStops: [
            { offset: 0, color: 'rgba(79, 172, 254, 0.3)' },
            { offset: 1, color: 'rgba(79, 172, 254, 0.05)' }
          ]
        }
      }
    }]
  }

  trendChart.setOption(option)
}

// 初始化地图
const initMapChart = async () => {
  if (!mapChartRef.value) return

  try {
    // 注册中国地图
    const response = await fetch('https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json')
    const chinaGeoJSON = await response.json()
    echarts.registerMap('china', chinaGeoJSON)
  } catch (error) {
    console.warn('地图数据加载失败，使用简化版本')
    // 使用备用地图数据
    try {
      const backupResponse = await fetch('https://unpkg.com/echarts@5/map/json/china.json')
      const backupGeoJSON = await backupResponse.json()
      echarts.registerMap('china', backupGeoJSON)
    } catch (backupError) {
      console.error('备用地图数据也加载失败')
      return
    }
  }

  mapChart = echarts.init(mapChartRef.value)

  // 模拟真实的省份销售数据
  const data = [
    { name: '北京', value: 567 },
    { name: '天津', value: 234 },
    { name: '上海', value: 623 },
    { name: '重庆', value: 298 },
    { name: '河北', value: 187 },
    { name: '河南', value: 356 },
    { name: '云南', value: 145 },
    { name: '辽宁', value: 267 },
    { name: '黑龙江', value: 123 },
    { name: '湖南', value: 389 },
    { name: '安徽', value: 278 },
    { name: '山东', value: 456 },
    { name: '新疆', value: 89 },
    { name: '江苏', value: 534 },
    { name: '浙江', value: 478 },
    { name: '江西', value: 234 },
    { name: '湖北', value: 312 },
    { name: '广西', value: 198 },
    { name: '甘肃', value: 67 },
    { name: '山西', value: 156 },
    { name: '内蒙古', value: 98 },
    { name: '陕西', value: 189 },
    { name: '吉林', value: 134 },
    { name: '福建', value: 345 },
    { name: '贵州', value: 123 },
    { name: '广东', value: 678 },
    { name: '青海', value: 45 },
    { name: '西藏', value: 23 },
    { name: '四川', value: 267 },
    { name: '宁夏', value: 56 },
    { name: '海南', value: 78 },
    { name: '台湾', value: 234 },
    { name: '香港', value: 156 },
    { name: '澳门', value: 89 }
  ]

  const option = {
    backgroundColor: 'transparent',
    tooltip: {
      trigger: 'item',
      formatter: function(params) {
        if (params.data && params.data.value) {
          return `
            <div style="
              background: rgba(15, 25, 45, 0.95);
              border: 1px solid rgba(79, 172, 254, 0.3);
              border-radius: 8px;
              padding: 12px 16px;
              box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
              backdrop-filter: blur(10px);
            ">
              <div style="color: #4facfe; font-weight: 600; font-size: 13px; margin-bottom: 4px;">
                📍 ${params.name}
              </div>
              <div style="color: #fff; font-size: 12px;">
                销售额: <span style="color: #43e97b; font-weight: 500;">${params.data.value}万元</span>
              </div>
            </div>
          `
        }
        return `
          <div style="
            background: rgba(15, 25, 45, 0.95);
            border: 1px solid rgba(255, 107, 122, 0.3);
            border-radius: 8px;
            padding: 12px 16px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(10px);
          ">
            <div style="color: #ff6b7a; font-weight: 600; font-size: 13px;">
              📍 ${params.name}
            </div>
            <div style="color: #a0aec0; font-size: 12px;">
              暂无数据
            </div>
          </div>
        `
      }
    },
    visualMap: {
      min: 0,
      max: 700,
      left: 'left',
      top: 'bottom',
      text: ['高', '低'],
      textStyle: {
        color: '#a0aec0'
      },
      inRange: {
        color: ['#1a202c', '#4a5568', '#ffa502', '#ff6b7a', '#ff4757']
      },
      show: false // 隐藏默认的视觉映射组件，使用自定义图例
    },
    series: [{
      name: '销售额',
      type: 'map',
      map: 'china',
      roam: false,
      zoom: 1.2,
      center: [105, 36],
      data: data,
      itemStyle: {
        borderColor: '#4a5568',
        borderWidth: 0.5
      },
      emphasis: {
        itemStyle: {
          areaColor: '#4facfe',
          borderColor: '#00f2fe',
          borderWidth: 1
        },
        label: {
          show: true,
          color: '#ffffff'
        }
      }
    }]
  }

  mapChart.setOption(option)
}

// 更新地图数据
const updateMapData = () => {
  if (!mapChart) return

  // 模拟数据变化
  const provinces = [
    '北京', '天津', '上海', '重庆', '河北', '河南', '云南', '辽宁', '黑龙江', '湖南',
    '安徽', '山东', '新疆', '江苏', '浙江', '江西', '湖北', '广西', '甘肃', '山西',
    '内蒙古', '陕西', '吉林', '福建', '贵州', '广东', '青海', '西藏', '四川', '宁夏',
    '海南', '台湾', '香港', '澳门'
  ]

  const newData = provinces.map(province => ({
    name: province,
    value: Math.floor(Math.random() * 600) + 50 // 50-650万的随机值
  }))

  mapChart.setOption({
    series: [{
      data: newData
    }]
  })
}

// 初始化排行图表
const initRankingChart = () => {
  if (!rankingChartRef.value) return

  rankingChart = echarts.init(rankingChartRef.value)

  const option = {
    backgroundColor: 'transparent',
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      top: '10%',
      containLabel: true
    },
    xAxis: {
      type: 'value',
      axisLine: { lineStyle: { color: '#4a5568' } },
      axisLabel: { color: '#a0aec0' },
      splitLine: { lineStyle: { color: '#2d3748' } }
    },
    yAxis: {
      type: 'category',
      data: ['产品E', '产品D', '产品C', '产品B', '产品A'],
      axisLine: { lineStyle: { color: '#4a5568' } },
      axisLabel: { color: '#a0aec0' }
    },
    series: [{
      type: 'bar',
      data: [220, 302, 181, 234, 290],
      itemStyle: {
        color: {
          type: 'linear',
          x: 0, y: 0, x2: 1, y2: 0,
          colorStops: [
            { offset: 0, color: '#4facfe' },
            { offset: 1, color: '#00f2fe' }
          ]
        }
      }
    }]
  }

  rankingChart.setOption(option)
}

// 初始化地区对比图表
const initRegionChart = () => {
  if (!regionChartRef.value) return

  regionChart = echarts.init(regionChartRef.value)

  const option = {
    backgroundColor: 'transparent',
    legend: {
      data: ['2023年', '2024年'],
      textStyle: { color: '#a0aec0' },
      top: '5%'
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      top: '20%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: ['华东', '华南', '华北', '西南', '西北'],
      axisLine: { lineStyle: { color: '#4a5568' } },
      axisLabel: { color: '#a0aec0' }
    },
    yAxis: {
      type: 'value',
      axisLine: { lineStyle: { color: '#4a5568' } },
      axisLabel: { color: '#a0aec0' },
      splitLine: { lineStyle: { color: '#2d3748' } }
    },
    series: [
      {
        name: '2023年',
        type: 'bar',
        data: [320, 302, 301, 334, 390],
        itemStyle: { color: '#f093fb' }
      },
      {
        name: '2024年',
        type: 'bar',
        data: [420, 382, 401, 434, 490],
        itemStyle: { color: '#4facfe' }
      }
    ]
  }

  regionChart.setOption(option)
}

// 窗口大小调整处理
const handleResize = () => {
  if (trendChart) trendChart.resize()
  if (mapChart) mapChart.resize()
  if (rankingChart) rankingChart.resize()
  if (regionChart) regionChart.resize()
}

// 组件挂载
onMounted(async () => {
  console.log('数字大屏初始化开始...')

  // 更新时间
  updateTime()
  timeTimer = setInterval(updateTime, 1000)

  // 生成初始实时数据
  for (let i = 0; i < 12; i++) {
    generateRealtimeData()
  }

  // 获取数据
  await fetchData()

  // 等待DOM渲染
  await nextTick()

  // 初始化图表
  setTimeout(async () => {
    initTrendChart()
    await initMapChart()
    initRankingChart()
    initRegionChart()
    console.log('图表初始化完成')
  }, 500)

  // 设置定时器
  dataTimer = setInterval(() => {
    generateRealtimeData()
    updateSystemMetrics()
    updateMapData() // 添加地图数据更新
  }, 3000)

  // 监听窗口大小变化
  window.addEventListener('resize', handleResize)

  console.log('数字大屏初始化完成')
})

// 组件卸载
onUnmounted(() => {
  if (timeTimer) clearInterval(timeTimer)
  if (dataTimer) clearInterval(dataTimer)

  if (trendChart) trendChart.dispose()
  if (mapChart) mapChart.dispose()
  if (rankingChart) rankingChart.dispose()
  if (regionChart) regionChart.dispose()

  window.removeEventListener('resize', handleResize)
})
</script>

<style scoped>
/* 全局样式 */
.data-screen {
  width: 100vw;
  height: 100vh;
  background: linear-gradient(135deg, #0c1426 0%, #1a202c 50%, #2d3748 100%);
  color: #ffffff;
  font-family: 'Microsoft YaHei', Arial, sans-serif;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
}

* {
  box-sizing: border-box;
}

/* 顶部标题栏 */
.screen-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 40px;
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.header-left {
  display: flex;
  flex-direction: column;
}

.screen-title {
  display: flex;
  align-items: center;
  margin: 0;
  font-size: 28px;
  font-weight: 600;
  background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.title-icon {
  margin-right: 12px;
  font-size: 32px;
}

.screen-subtitle {
  margin: 5px 0 0 44px;
  font-size: 14px;
  color: #a0aec0;
  text-transform: uppercase;
  letter-spacing: 2px;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 30px;
}

.time-display {
  text-align: right;
}

.current-time {
  font-size: 24px;
  font-weight: 600;
  color: #4facfe;
}

.current-date {
  font-size: 14px;
  color: #a0aec0;
  margin-top: 4px;
}

.status-indicator {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background: rgba(79, 172, 254, 0.1);
  border: 1px solid rgba(79, 172, 254, 0.3);
  border-radius: 20px;
}

.status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #ff6b7a;
  animation: pulse 2s infinite;
}

.status-dot.active {
  background: #43e97b;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

/* 主要内容区域 */
.screen-main {
  flex: 1;
  padding: 20px 40px;
  overflow-y: auto;
  overflow-x: hidden;
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 100%;
  box-sizing: border-box;
}

/* 统计卡片区域 */
.stats-section {
  margin-bottom: 20px;
  width: 100%;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  width: 100%;
}

.stat-card {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  padding: 24px;
  display: flex;
  align-items: center;
  gap: 20px;
  transition: all 0.3s ease;
  animation: fadeInUp 0.6s ease forwards;
  opacity: 0;
  transform: translateY(20px);
}

.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 32px rgba(79, 172, 254, 0.2);
  border-color: rgba(79, 172, 254, 0.3);
}

.stat-icon {
  width: 60px;
  height: 60px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  flex-shrink: 0;
}

.stat-content {
  flex: 1;
}

.stat-label {
  font-size: 14px;
  color: #a0aec0;
  margin-bottom: 8px;
}

.stat-value {
  font-size: 28px;
  font-weight: 600;
  color: #ffffff;
  margin-bottom: 4px;
}

.stat-change {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
}

.stat-change.positive {
  color: #43e97b;
}

.stat-change.negative {
  color: #ff6b7a;
}

@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 图表区域 */
.charts-section {
  margin-bottom: 20px;
  width: 100%;
}

.charts-grid {
  display: grid;
  grid-template-columns: 1fr 1.5fr 1fr;
  gap: 20px;
  min-height: 400px;
  width: 100%;
}

.chart-card {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  transition: all 0.3s ease;
}

.chart-card:hover {
  border-color: rgba(79, 172, 254, 0.3);
  box-shadow: 0 4px 20px rgba(79, 172, 254, 0.1);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.card-header h3 {
  margin: 0;
  font-size: 18px;
  font-weight: 600;
  color: #ffffff;
}

.time-filter {
  display: flex;
  gap: 8px;
}

.time-filter button {
  padding: 6px 12px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 6px;
  color: #a0aec0;
  font-size: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.time-filter button:hover,
.time-filter button.active {
  background: rgba(79, 172, 254, 0.2);
  border-color: rgba(79, 172, 254, 0.5);
  color: #4facfe;
}

.map-legend {
  display: flex;
  gap: 16px;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  color: #a0aec0;
}

.legend-color {
  width: 12px;
  height: 12px;
  border-radius: 2px;
}

.live-indicator {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #43e97b;
  font-size: 12px;
  font-weight: 600;
}

.live-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #43e97b;
  animation: pulse 1.5s infinite;
}

.chart-container {
  flex: 1;
  min-height: 0;
}

/* 实时数据容器 */
.realtime-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: 0;
}

/* 实时数据列表 */
.realtime-list {
  flex: 1;
  overflow-y: auto;
  overflow-x: hidden;
  max-height: 240px;
  padding-right: 8px;
  margin-right: -8px;
}

.realtime-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  animation: slideInRight 0.5s ease;
  transition: background-color 0.2s ease;
}

.realtime-item:hover {
  background-color: rgba(255, 255, 255, 0.02);
  border-radius: 6px;
  padding-left: 6px;
  padding-right: 6px;
}

.realtime-item:last-child {
  border-bottom: none;
}

.item-avatar {
  width: 28px;
  height: 28px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  font-weight: 600;
  font-size: 12px;
  flex-shrink: 0;
}

.item-content {
  flex: 1;
  min-width: 0;
}

.item-region {
  font-size: 13px;
  color: #ffffff;
  margin-bottom: 2px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.item-amount {
  font-size: 11px;
  color: #4facfe;
  font-weight: 600;
}

.item-time {
  font-size: 10px;
  color: #a0aec0;
  flex-shrink: 0;
}

/* 实时统计 */
.realtime-stats {
  margin-top: 12px;
  padding-top: 12px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.stats-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.stats-label {
  font-size: 11px;
  color: #a0aec0;
}

.stats-value {
  font-size: 12px;
  color: #43e97b;
  font-weight: 600;
}

@keyframes slideInRight {
  from {
    opacity: 0;
    transform: translateX(20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* 底部区域 */
.bottom-section {
  margin-top: 20px;
  width: 100%;
}

.bottom-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 20px;
  min-height: 280px;
  width: 100%;
}

/* 系统监控面板 */
.monitor-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.monitor-item {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.metric-label {
  font-size: 14px;
  color: #a0aec0;
}

.metric-value {
  font-size: 18px;
  font-weight: 600;
  color: #ffffff;
  word-break: break-all;
  overflow: hidden;
  text-overflow: ellipsis;
}

.metric-bar {
  height: 6px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 3px;
  overflow: hidden;
}

.metric-progress {
  height: 100%;
  border-radius: 3px;
  transition: width 0.5s ease;
}

/* 底部状态栏 */
.screen-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 40px;
  background: rgba(0, 0, 0, 0.3);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 12px;
  color: #a0aec0;
}

.footer-left {
  display: flex;
  gap: 16px;
}

/* 响应式设计 */
@media (max-width: 1400px) {
  .charts-grid {
    grid-template-columns: 1fr;
    grid-template-rows: auto auto auto;
    min-height: auto;
    gap: 16px;
  }

  .chart-card {
    min-height: 300px;
    height: auto;
  }

  .bottom-grid {
    grid-template-columns: 1fr;
    min-height: auto;
  }

  .bottom-grid .chart-card {
    min-height: 250px;
    height: auto;
  }
}

@media (max-width: 1200px) {
  .charts-grid {
    grid-template-columns: 1fr 1fr;
    grid-template-rows: auto auto;
  }

  .realtime-data {
    grid-column: 1 / -1;
  }
}

@media (max-width: 1024px) {
  .screen-header {
    padding: 16px 24px;
  }

  .screen-main {
    padding: 16px 24px;
  }

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
  }

  .charts-grid {
    grid-template-columns: 1fr;
    gap: 16px;
  }

  .bottom-grid {
    grid-template-columns: 1fr;
    gap: 16px;
  }

  .screen-title {
    font-size: 24px;
  }

  .current-time {
    font-size: 20px;
  }

  .screen-footer {
    padding: 12px 24px;
    flex-direction: column;
    gap: 8px;
  }
}

@media (max-width: 768px) {
  .screen-header {
    flex-direction: column;
    gap: 16px;
    text-align: center;
  }

  .header-right {
    gap: 20px;
  }

  .stats-grid {
    grid-template-columns: 1fr;
  }

  .stat-card {
    padding: 20px;
  }

  .stat-icon {
    width: 50px;
    height: 50px;
    font-size: 20px;
  }

  .stat-value {
    font-size: 24px;
  }

  .chart-card {
    padding: 16px;
  }

  .card-header {
    flex-direction: column;
    gap: 12px;
    align-items: flex-start;
  }

  .map-legend {
    flex-wrap: wrap;
    gap: 12px;
  }

  .realtime-list {
    max-height: 200px;
  }

  .realtime-item {
    padding: 6px 0;
  }

  .item-avatar {
    width: 24px;
    height: 24px;
    font-size: 10px;
  }

  .item-region {
    font-size: 12px;
  }

  .item-amount {
    font-size: 10px;
  }

  .item-time {
    font-size: 9px;
  }

  .stats-label {
    font-size: 10px;
  }

  .stats-value {
    font-size: 11px;
  }
}

/* 滚动条样式 */
::-webkit-scrollbar {
  width: 4px;
}

::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 2px;
}

::-webkit-scrollbar-thumb {
  background: rgba(79, 172, 254, 0.4);
  border-radius: 2px;
  transition: background 0.3s ease;
}

::-webkit-scrollbar-thumb:hover {
  background: rgba(79, 172, 254, 0.6);
}

/* 实时数据列表专用滚动条 */
.realtime-list::-webkit-scrollbar {
  width: 3px;
}

.realtime-list::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.03);
  border-radius: 2px;
}

.realtime-list::-webkit-scrollbar-thumb {
  background: rgba(79, 172, 254, 0.3);
  border-radius: 2px;
}

.realtime-list::-webkit-scrollbar-thumb:hover {
  background: rgba(79, 172, 254, 0.5);
}
</style>
