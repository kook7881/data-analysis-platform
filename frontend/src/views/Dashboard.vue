<template>
  <div class="dashboard-container">
    <div class="dashboard-header">
      <h2>数据仪表盘</h2>
      <button class="refresh-btn" @click="refreshData">
        <span class="refresh-icon">🔄</span>
        <span>刷新数据</span>
      </button>
    </div>

    <div class="metrics-wrapper" v-loading="loading">
      <!-- 关键指标卡片 -->
      <div v-if="!dashboardData" class="loading-state">
        <div class="loading-icon">⏳</div>
        <p>正在加载数据...</p>
      </div>
      <div v-else class="metrics-grid">
        <div class="metric-card" v-for="(metric, index) in dashboardData.metrics" :key="index">
          <div class="metric-icon" :class="`metric-icon-${index+1}`">
            <span v-if="index === 0">💰</span>
            <span v-else-if="index === 1">👥</span>
            <span v-else-if="index === 2">📦</span>
            <span v-else>💵</span>
          </div>
          <div class="metric-content">
            <div class="metric-value">{{ metric.value }}</div>
            <div class="metric-title">{{ metric.title }}</div>
            <div class="metric-change" :class="metric.change > 0 ? 'positive' : 'negative'">
              {{ metric.change > 0 ? '+' : '' }}{{ metric.change }}%
              <span class="change-icon">{{ metric.change > 0 ? '↑' : '↓' }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="charts-container" v-if="dashboardData">
      <el-row :gutter="20" class="chart-row">
        <!-- 销售趋势图 -->
        <el-col :span="12">
          <el-card class="chart-card">
            <div class="card-header" slot="header">
              <span>销售趋势</span>
            </div>
            <div class="chart-container" ref="salesChartRef"></div>
          </el-card>
        </el-col>
        
        <!-- 用户分布饼图 -->
        <el-col :span="12">
          <el-card class="chart-card">
            <div class="card-header" slot="header">
              <span>用户分布</span>
            </div>
            <div class="chart-container" ref="userChartRef"></div>
          </el-card>
        </el-col>
      </el-row>

      <el-row :gutter="20" class="chart-row">
        <!-- 产品销售柱状图 -->
        <el-col :span="24">
          <el-card class="chart-card">
            <div class="card-header" slot="header">
              <span>产品销售量</span>
            </div>
            <div class="chart-container" ref="productChartRef"></div>
          </el-card>
        </el-col>
      </el-row>
    </div>
    
    <div v-if="apiError" class="api-error">
      <div class="error-icon">⚠️</div>
      <div class="error-message">
        <h3>连接后端服务失败</h3>
        <p>{{ apiError }}</p>
        <p>已显示模拟数据，请检查后端服务状态或网络连接</p>
        <div class="error-actions">
          <button class="retry-btn" @click="refreshData">
            <span class="btn-icon">🔄</span> 重试连接
          </button>
          <button class="toggle-btn" @click="toggleMockData">
            使用{{ useMockData ? '真实' : '模拟' }}数据
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { useDataStore } from '../store'
import * as echarts from 'echarts'

const dataStore = useDataStore()
const loading = ref(false)
const apiError = ref(null)
const salesChartRef = ref(null)
const userChartRef = ref(null)
const productChartRef = ref(null)

let salesChart = null
let userChart = null
let productChart = null

// 从store中获取仪表盘数据
const dashboardData = computed(() => dataStore.getDashboardData)
// 是否使用模拟数据
const useMockData = computed(() => dataStore.useMockData)

// 切换模拟/真实数据
const toggleMockData = () => {
  dataStore.toggleMockData()
  refreshData()
}

// 初始化图表
const initCharts = () => {
  if (!dashboardData.value) return

  // 销售趋势图
  if (salesChartRef.value && !salesChart) {
    salesChart = echarts.init(salesChartRef.value)
  }
  
  if (salesChart) {
    salesChart.setOption({
      tooltip: {
        trigger: 'axis'
      },
      xAxis: {
        type: 'category',
        data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月']
      },
      yAxis: {
        type: 'value'
      },
      series: [
        {
          name: '销售额',
          type: 'line',
          smooth: true,
          data: dashboardData.value.salesTrend,
          areaStyle: {
            opacity: 0.3
          },
          lineStyle: {
            width: 3
          },
          itemStyle: {
            color: '#409EFF'
          }
        }
      ]
    })
  }

  // 用户分布饼图
  if (userChartRef.value && !userChart) {
    userChart = echarts.init(userChartRef.value)
  }
  
  if (userChart) {
    userChart.setOption({
      tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b}: {c} ({d}%)'
      },
      legend: {
        orient: 'vertical',
        left: 'left',
        data: dashboardData.value.userDistribution.map(item => item.name)
      },
      series: [
        {
          name: '用户分布',
          type: 'pie',
          radius: '70%',
          center: ['50%', '50%'],
          data: dashboardData.value.userDistribution,
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowOffsetX: 0,
              shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
          }
        }
      ]
    })
  }

  // 产品销售柱状图
  if (productChartRef.value && !productChart) {
    productChart = echarts.init(productChartRef.value)
  }
  
  if (productChart) {
    productChart.setOption({
      tooltip: {
        trigger: 'axis',
        axisPointer: {
          type: 'shadow'
        }
      },
      legend: {
        data: ['2022年', '2023年']
      },
      xAxis: {
        type: 'category',
        data: ['产品A', '产品B', '产品C', '产品D', '产品E']
      },
      yAxis: {
        type: 'value'
      },
      series: [
        {
          name: '2022年',
          type: 'bar',
          data: dashboardData.value.productSales.lastYear
        },
        {
          name: '2023年',
          type: 'bar',
          data: dashboardData.value.productSales.currentYear
        }
      ]
    })
  }
}

// 处理窗口大小变化
const handleResize = () => {
  salesChart && salesChart.resize()
  userChart && userChart.resize()
  productChart && productChart.resize()
}

// 刷新数据
const refreshData = async () => {
  loading.value = true
  apiError.value = null

  try {
    await dataStore.fetchDashboardData()
    
    // 等待DOM更新后初始化图表
    setTimeout(() => {
      loading.value = false
      initCharts()
    }, 100)
  } catch (error) {
    console.error('Failed to fetch dashboard data:', error)
    apiError.value = error.message || '获取数据失败，请稍后再试'
    loading.value = false
  }
}

onMounted(() => {
  refreshData()
  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  salesChart && salesChart.dispose()
  userChart && userChart.dispose()
  productChart && productChart.dispose()
})
</script>

<style scoped>
.dashboard-container {
  padding: 20px;
  max-width: 1280px;
  margin: 0 auto;
}

.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
  padding-bottom: 16px;
  border-bottom: 1px solid #ebeef5;
}

.dashboard-header h2 {
  font-size: 1.8rem;
  color: #1976D2;
  margin: 0;
  font-weight: 600;
}

.refresh-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  background-color: #1976D2;
  color: white;
  border: none;
  padding: 10px 16px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.3s;
}

.refresh-btn:hover {
  background-color: #1565C0;
}

.refresh-icon {
  font-size: 16px;
}

/* 加载状态 */
.loading-state {
  height: 200px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #909399;
}

.loading-icon {
  font-size: 3rem;
  margin-bottom: 16px;
  animation: spin 2s infinite linear;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* 指标卡片样式 */
.metrics-wrapper {
  position: relative;
  margin-bottom: 24px;
}

.metrics-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}

.metric-card {
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  padding: 20px;
  display: flex;
  align-items: center;
  gap: 16px;
  transition: all 0.3s;
  border: 1px solid #f0f0f0;
  height: 100%;
}

.metric-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
}

.metric-icon {
  width: 50px;
  height: 50px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
}

.metric-icon-1 {
  background-color: rgba(25, 118, 210, 0.1);
  color: #1976D2;
}

.metric-icon-2 {
  background-color: rgba(56, 142, 60, 0.1);
  color: #388E3C;
}

.metric-icon-3 {
  background-color: rgba(245, 124, 0, 0.1);
  color: #F57C00;
}

.metric-icon-4 {
  background-color: rgba(123, 31, 162, 0.1);
  color: #7B1FA2;
}

.metric-content {
  flex: 1;
}

.metric-value {
  font-size: 24px;
  font-weight: bold;
  color: #303133;
  line-height: 1.2;
}

.metric-title {
  font-size: 14px;
  color: #909399;
  margin: 4px 0 8px;
}

.metric-change {
  font-size: 13px;
  display: flex;
  align-items: center;
}

.change-icon {
  margin-left: 4px;
}

.positive {
  color: #67C23A;
}

.negative {
  color: #F56C6C;
}

/* API错误提示 */
.api-error {
  background-color: #FFF8F0;
  border: 1px solid #FFEBCC;
  border-radius: 8px;
  padding: 20px;
  margin-top: 24px;
  display: flex;
  gap: 16px;
  align-items: flex-start;
}

.error-icon {
  font-size: 24px;
  color: #E6A23C;
}

.error-message h3 {
  margin: 0 0 8px 0;
  color: #E6A23C;
  font-size: 16px;
}

.error-message p {
  margin: 0 0 8px 0;
  color: #606266;
  font-size: 14px;
}

.error-actions {
  display: flex;
  gap: 12px;
  margin-top: 16px;
}

.retry-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  background-color: #E6A23C;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.3s;
}

.retry-btn:hover {
  background-color: #D48806;
}

.toggle-btn {
  background-color: white;
  color: #606266;
  border: 1px solid #DCDFE6;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.3s;
}

.toggle-btn:hover {
  color: #409EFF;
  border-color: #c6e2ff;
  background-color: #ecf5ff;
}

/* 图表容器样式 */
.charts-container {
  margin-top: 30px;
}

.chart-row {
  margin-bottom: 20px;
}

.chart-card {
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  border: none;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 16px;
  font-weight: 600;
  color: #303133;
}

.chart-container {
  height: 350px;
  width: 100%;
}

/* 响应式样式 */
@media (max-width: 1200px) {
  .metrics-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .metrics-grid {
    grid-template-columns: 1fr;
  }
  
  .chart-row .el-col {
    width: 100%;
  }
  
  .error-actions {
    flex-direction: column;
  }
}
</style> 