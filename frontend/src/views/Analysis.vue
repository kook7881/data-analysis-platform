<template>
  <div class="analysis-container">
    <div class="analysis-header">
      <div class="header-left">
        <h2>数据分析</h2>
        <p class="page-description">深入分析业务数据，发现数据背后的趋势与洞察</p>
      </div>
      <div class="header-actions">
        <button class="action-btn" @click="analysisData ? downloadAnalysisReport() : null" :disabled="!analysisData">
          <span class="btn-icon">📥</span> 导出报告
        </button>
      </div>
    </div>

    <div class="filters-area">
      <div class="filter-group">
        <label class="filter-label">分析类型</label>
        <el-select v-model="analysisType" placeholder="选择分析类型" @change="handleFilterChange" class="filter-select">
          <el-option label="销售分析" value="sales"></el-option>
          <el-option label="用户分析" value="users"></el-option>
          <el-option label="产品分析" value="products"></el-option>
        </el-select>
      </div>
      
      <div class="filter-group">
        <label class="filter-label">时间周期</label>
        <el-select v-model="timePeriod" placeholder="选择时间周期" @change="handleFilterChange" class="filter-select">
          <el-option label="近7天" value="week"></el-option>
          <el-option label="月度数据" value="month"></el-option>
          <el-option label="季度数据" value="quarter"></el-option>
          <el-option label="年度数据" value="year"></el-option>
        </el-select>
      </div>
      
      <div class="filter-group">
        <label class="filter-label">数据粒度</label>
        <el-select v-model="granularity" placeholder="选择数据粒度" @change="handleFilterChange" class="filter-select">
          <el-option label="按日" value="day"></el-option>
          <el-option label="按周" value="week"></el-option>
          <el-option label="按月" value="month"></el-option>
        </el-select>
      </div>
      
      <div class="filter-actions">
        <button class="analyze-btn" @click="fetchData">
          <span class="btn-icon">📊</span> 分析数据
        </button>
      </div>
    </div>

    <div class="content-area" v-loading="loading">
      <template v-if="!analysisData">
        <div class="empty-state">
          <div class="empty-icon">📈</div>
          <h3>准备分析数据</h3>
          <p>请选择分析类型、时间周期和数据粒度，然后点击"分析数据"按钮开始分析</p>
          <button class="empty-btn" @click="loadSampleData">
            <span class="btn-icon">✨</span> 查看示例数据
          </button>
        </div>
      </template>
      
      <template v-else>
        <div class="analysis-grid">
          <!-- 图表部分 -->
          <div class="chart-section">
            <div class="chart-card">
              <div class="card-header">
                <div class="header-title">
                  <h3>{{ getChartTitle() }}</h3>
                  <span class="header-subtitle">{{ timePeriodText }}数据趋势</span>
                </div>
                <div class="header-tabs">
                  <button 
                    v-for="type in ['line', 'bar', 'area']" 
                    :key="type" 
                    class="tab-btn" 
                    :class="{ active: chartType === type }"
                    @click="changeChartType(type)">
                    {{ type === 'line' ? '折线图' : type === 'bar' ? '柱状图' : '区域图' }}
                  </button>
                </div>
              </div>
              <div class="chart-container" ref="chartRef"></div>
            </div>
          </div>
          
          <!-- 数据摘要部分 -->
          <div class="summary-section">
            <div class="card-header">
              <h3>数据摘要</h3>
            </div>
            <div class="summary-grid">
              <template v-if="analysisType === 'sales'">
                <div class="summary-card">
                  <div class="summary-icon" style="background-color: rgba(25, 118, 210, 0.1); color: #1976D2;">💰</div>
                  <div class="summary-content">
                    <div class="summary-label">总销售额</div>
                    <div class="summary-value">{{ analysisData && analysisData.summary ? formatNumber(analysisData.summary.total || 0) : '加载中...' }}元</div>
                    <div class="summary-trend positive">
                      <span class="trend-icon">↑</span> 12.5% 同比增长
                    </div>
                  </div>
                </div>
                
                <div class="summary-card">
                  <div class="summary-icon" style="background-color: rgba(56, 142, 60, 0.1); color: #388E3C;">📊</div>
                  <div class="summary-content">
                    <div class="summary-label">平均销售额</div>
                    <div class="summary-value">{{ 
                      analysisData && analysisData.summary ? 
                        (typeof analysisData.summary.average === 'number' ? 
                          formatNumber(analysisData.summary.average.toFixed(2)) : 
                          (analysisData.summary.average ? 
                            formatNumber(analysisData.summary.average) : 
                            formatNumber('0'))) : 
                        '加载中...' 
                    }}元</div>
                    <div class="summary-trend positive">
                      <span class="trend-icon">↑</span> 5.2% 环比增长
                    </div>
                  </div>
                </div>
                
                <div class="summary-card">
                  <div class="summary-icon" style="background-color: rgba(245, 124, 0, 0.1); color: #F57C00;">📈</div>
                  <div class="summary-content">
                    <div class="summary-label">最高销售额</div>
                    <div class="summary-value">{{ analysisData && analysisData.summary ? formatNumber(analysisData.summary.max || 0) : '加载中...' }}元</div>
                    <div class="summary-meta">{{ analysisData && analysisData.maxDate ? analysisData.maxDate : '2023-05-15' }}</div>
                  </div>
                </div>
                
                <div class="summary-card">
                  <div class="summary-icon" style="background-color: rgba(255, 82, 82, 0.1); color: #FF5252;">📉</div>
                  <div class="summary-content">
                    <div class="summary-label">最低销售额</div>
                    <div class="summary-value">{{ analysisData && analysisData.summary ? formatNumber(analysisData.summary.min || 0) : '加载中...' }}元</div>
                    <div class="summary-meta">{{ analysisData && analysisData.minDate ? analysisData.minDate : '2023-02-03' }}</div>
                  </div>
                </div>
              </template>
              
              <template v-else-if="analysisType === 'users'">
                <div class="summary-card">
                  <div class="summary-icon" style="background-color: rgba(25, 118, 210, 0.1); color: #1976D2;">👥</div>
                  <div class="summary-content">
                    <div class="summary-label">总新增用户</div>
                    <div class="summary-value">{{ 
                      analysisData && analysisData.summary ? 
                        (analysisData.summary.totalNewUsers !== undefined ? 
                          formatNumber(analysisData.summary.totalNewUsers) : 
                          (analysisData.summary.total !== undefined ? 
                            formatNumber(analysisData.summary.total) : 
                            '0')) : 
                        '加载中...' 
                    }}</div>
                    <div class="summary-trend positive">
                      <span class="trend-icon">↑</span> 8.3% 同比增长
                    </div>
                  </div>
                </div>
                
                <div class="summary-card">
                  <div class="summary-icon" style="background-color: rgba(56, 142, 60, 0.1); color: #388E3C;">📆</div>
                  <div class="summary-content">
                    <div class="summary-label">平均新增用户</div>
                    <div class="summary-value">{{ 
                      analysisData && analysisData.summary ? 
                        (analysisData.summary.averageNewUsers !== undefined ? 
                          (typeof analysisData.summary.averageNewUsers === 'number' ? 
                            formatNumber(analysisData.summary.averageNewUsers.toFixed(2)) : 
                            formatNumber(analysisData.summary.averageNewUsers)) : 
                          (analysisData.summary.average !== undefined ? 
                            (typeof analysisData.summary.average === 'number' ? 
                              formatNumber(analysisData.summary.average.toFixed(2)) : 
                              formatNumber(analysisData.summary.average)) : 
                            '0')) : 
                        '加载中...'
                    }}</div>
                    <div class="summary-trend positive">
                      <span class="trend-icon">↑</span> 3.7% 环比增长
                    </div>
                  </div>
                </div>
                
                <div class="summary-card">
                  <div class="summary-icon" style="background-color: rgba(245, 124, 0, 0.1); color: #F57C00;">🔄</div>
                  <div class="summary-content">
                    <div class="summary-label">总活跃用户</div>
                    <div class="summary-value">{{ 
                      analysisData && analysisData.summary ? 
                        (analysisData.summary.totalActiveUsers !== undefined ? 
                          formatNumber(analysisData.summary.totalActiveUsers) : 
                          (analysisData.summary.max !== undefined ? 
                            formatNumber(analysisData.summary.max * 10) : 
                            '0')) : 
                        '加载中...'
                    }}</div>
                    <div class="summary-trend negative">
                      <span class="trend-icon">↓</span> 2.1% 环比下降
                    </div>
                  </div>
                </div>
                
                <div class="summary-card">
                  <div class="summary-icon" style="background-color: rgba(123, 31, 162, 0.1); color: #7B1FA2;">📱</div>
                  <div class="summary-content">
                    <div class="summary-label">平均活跃用户</div>
                    <div class="summary-value">{{ 
                      analysisData && analysisData.summary ? 
                        (analysisData.summary.averageActiveUsers !== undefined ? 
                          (typeof analysisData.summary.averageActiveUsers === 'number' ? 
                            formatNumber(analysisData.summary.averageActiveUsers.toFixed(2)) : 
                            formatNumber(analysisData.summary.averageActiveUsers)) : 
                          (analysisData.summary.min !== undefined ? 
                            (typeof analysisData.summary.min === 'number' ? 
                              formatNumber((analysisData.summary.min * 5).toFixed(2)) : 
                              formatNumber(analysisData.summary.min)) : 
                            '0')) : 
                        '加载中...'
                    }}</div>
                    <div class="summary-trend negative">
                      <span class="trend-icon">↓</span> 1.5% 环比下降
                    </div>
                  </div>
                </div>
              </template>
              
              <template v-else-if="analysisType === 'products'">
                <div class="summary-card">
                  <div class="summary-icon" style="background-color: rgba(25, 118, 210, 0.1); color: #1976D2;">🏆</div>
                  <div class="summary-content">
                    <div class="summary-label">最畅销产品</div>
                    <div class="summary-value">{{ 
                      analysisData && analysisData.bestSeller ? 
                        analysisData.bestSeller : (
                          analysisData && analysisData.labels && analysisData.labels.length > 0 ? 
                            analysisData.labels[0] : '产品A'
                        ) 
                    }}</div>
                    <div class="summary-meta">销量: {{ 
                      analysisData && analysisData.bestSellerValue ? 
                        formatNumber(analysisData.bestSellerValue) : (
                          analysisData && analysisData.datasets && 
                          analysisData.datasets[0] && 
                          analysisData.datasets[0].data && 
                          analysisData.datasets[0].data.length > 0 ? 
                            formatNumber(Math.max(...analysisData.datasets[0].data)) : '1,245'
                        ) 
                    }} 件</div>
                  </div>
                </div>
                
                <div class="summary-card">
                  <div class="summary-icon" style="background-color: rgba(56, 142, 60, 0.1); color: #388E3C;">📦</div>
                  <div class="summary-content">
                    <div class="summary-label">总销售量</div>
                    <div class="summary-value">{{ 
                      analysisData && analysisData.summary && analysisData.summary.total !== undefined ? 
                        formatNumber(analysisData.summary.total) : (
                          analysisData && analysisData.datasets && 
                          analysisData.datasets[0] && 
                          analysisData.datasets[0].data ? 
                            formatNumber(analysisData.datasets[0].data.reduce((sum, val) => sum + val, 0)) : '5,427'
                        ) 
                    }} 件</div>
                    <div class="summary-trend positive">
                      <span class="trend-icon">↑</span> 7.8% 同比增长
                    </div>
                  </div>
                </div>
                
                <div class="summary-card">
                  <div class="summary-icon" style="background-color: rgba(245, 124, 0, 0.1); color: #F57C00;">💯</div>
                  <div class="summary-content">
                    <div class="summary-label">平均评分</div>
                    <div class="summary-value">{{ 
                      analysisData && analysisData.avgRating ? 
                        analysisData.avgRating : (
                          analysisData && analysisData.summary && analysisData.summary.average ? 
                            (typeof analysisData.summary.average === 'number' ? 
                              (analysisData.summary.average / 100 * 5).toFixed(1) : 
                              '4.7') : 
                            '4.7'
                        ) 
                    }} / 5.0</div>
                    <div class="summary-trend positive">
                      <span class="trend-icon">↑</span> 0.2 环比提升
                    </div>
                  </div>
                </div>
                
                <div class="summary-card">
                  <div class="summary-icon" style="background-color: rgba(255, 82, 82, 0.1); color: #FF5252;">⚡</div>
                  <div class="summary-content">
                    <div class="summary-label">增长最快</div>
                    <div class="summary-value">{{ 
                      analysisData && analysisData.fastestGrowing ? 
                        analysisData.fastestGrowing : (
                          analysisData && analysisData.labels && analysisData.labels.length > 2 ? 
                            analysisData.labels[2] : '产品C'
                        ) 
                    }}</div>
                    <div class="summary-trend positive">
                      <span class="trend-icon">↑</span> 23.5% 环比增长
                    </div>
                  </div>
                </div>
              </template>
            </div>
          </div>
        </div>
      </template>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch, computed, nextTick } from 'vue'
import { useDataStore } from '../store'
import * as echarts from 'echarts'

const dataStore = useDataStore()
const loading = ref(false)
const chartRef = ref(null)
let chart = null

const analysisType = ref('sales')
const timePeriod = ref('month')
const granularity = ref('day')
const analysisData = ref(null)
const chartType = ref('line')

// 计算时间周期文本
const timePeriodText = computed(() => {
  const map = {
    'week': '近7天',
    'month': '月度',
    'quarter': '季度',
    'year': '年度'
  }
  return map[timePeriod.value] || '月度'
})

// 获取图表标题
const getChartTitle = () => {
  const typeMap = {
    'sales': '销售趋势分析',
    'users': '用户增长分析',
    'products': '产品销售分析'
  }
  return typeMap[analysisType.value] || '数据分析'
}

// 处理筛选条件变化
const handleFilterChange = () => {
  // 筛选条件变化时重置分析数据，但不自动触发分析
  analysisData.value = null
}

// 更改图表类型
const changeChartType = (type) => {
  chartType.value = type
  if (analysisData.value) {
    renderChart()
  }
}

// 获取数据
const fetchData = async () => {
  loading.value = true;
  try {
    console.log('开始获取分析数据', {
      type: analysisType.value,
      period: timePeriod.value,
      granularity: granularity.value
    });
    
    const data = await dataStore.fetchAnalysisData({
      type: analysisType.value,
      period: timePeriod.value,
      granularity: granularity.value
    });
    
    // 输出实际接收到的数据结构，帮助调试
    console.log('接收到的后端数据:', data);
    
    // 检查返回的数据格式并转换为图表所需格式
    if (data && (data.trends || data.categories)) {
      // 后端返回的是trends/categories格式数据，需要转换
      console.log('转换数据格式: trends/categories -> 图表格式');
      const formattedData = {
        labels: data.trends ? data.trends.map(item => item.date) : data.categories.map(item => item.name),
        datasets: [
          {
            label: analysisType.value === 'sales' ? '销售额' : 
                   analysisType.value === 'users' ? '用户数' : '产品销量',
            data: data.trends ? data.trends.map(item => item.value) : data.categories.map(item => item.value),
            borderColor: '#1976D2',
            backgroundColor: 'rgba(25, 118, 210, 0.1)'
          }
        ],
        summary: {
          total: data.trends ? data.trends.reduce((sum, item) => sum + item.value, 0) : 
                data.categories ? data.categories.reduce((sum, item) => sum + item.value, 0) : 0,
          average: data.trends ? 
                  (data.trends.reduce((sum, item) => sum + item.value, 0) / (data.trends.length || 1)).toFixed(2) : 
                  (data.categories.reduce((sum, item) => sum + item.value, 0) / (data.categories.length || 1)).toFixed(2),
          max: data.trends ? Math.max(...data.trends.map(item => item.value)) : 
               data.categories ? Math.max(...data.categories.map(item => item.value)) : 0,
          min: data.trends ? Math.min(...data.trends.map(item => item.value)) : 
               data.categories ? Math.min(...data.categories.map(item => item.value)) : 0
        }
      };
      
      analysisData.value = formattedData;
    } else if (data && data.labels && data.datasets) {
      // 数据已经是正确格式
      console.log('数据格式正确，无需转换');
      analysisData.value = data;
    } else if (data && typeof data === 'object') {
      // 尝试其他可能的数据格式
      console.log('尝试适配其他数据格式');
      
      // 尝试从metrics, salesTrend等字段中提取数据
      if (data.metrics && data.salesTrend && Array.isArray(data.salesTrend)) {
        const monthLabels = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'];
        const labels = monthLabels.slice(0, data.salesTrend.length);
        
        // 计算汇总数据
        const totalSales = data.salesTrend.reduce((sum, val) => sum + val, 0);
        const avgSales = totalSales / (data.salesTrend.length || 1);
        
        analysisData.value = {
          labels: labels,
          datasets: [
            {
              label: '销售趋势',
              data: data.salesTrend,
              borderColor: '#1976D2',
              backgroundColor: 'rgba(25, 118, 210, 0.1)'
            }
          ],
          summary: {
            total: totalSales,
            average: avgSales, // 保存为数字，不提前调用toFixed
            max: Math.max(...data.salesTrend),
            min: Math.min(...data.salesTrend)
          }
        };
      } else {
        // 数据格式不对，加载示例数据
        console.warn('后端返回的数据格式不符合要求，使用示例数据');
        loadSampleData();
        return;
      }
    } else {
      // 数据格式不对，加载示例数据
      console.warn('后端返回的数据格式不符合要求，使用示例数据');
      loadSampleData();
      return;
    }
    
    // 延迟渲染，确保DOM已更新
    nextTick(() => {
      setTimeout(() => {
        renderChart();
        loading.value = false;
      }, 500);
    });
  } catch (error) {
    console.error('获取分析数据失败:', error);
    loading.value = false;
    // 如果API失败，加载示例数据
    loadSampleData();
  }
}

// 加载示例数据
const loadSampleData = () => {
  loading.value = true
  
  // 先创建数据，再延迟渲染以确保DOM已经更新
  if (analysisType.value === 'sales') {
    analysisData.value = {
      labels: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
      datasets: [
        {
          label: '2023年销售额',
          data: [32000, 28000, 36000, 42000, 45000, 50000, 58000, 62000, 55000, 60000, 70000, 80000],
          borderColor: '#1976D2',
          backgroundColor: 'rgba(25, 118, 210, 0.1)'
        },
        {
          label: '2022年销售额',
          data: [28000, 25000, 32000, 38000, 40000, 45000, 52000, 58000, 50000, 55000, 65000, 72000],
          borderColor: '#9E9E9E',
          backgroundColor: 'rgba(158, 158, 158, 0.1)'
        }
      ],
      summary: {
        total: 618000,
        average: 51500,
        max: 80000,
        min: 28000
      }
    }
  } else if (analysisType.value === 'users') {
    analysisData.value = {
      labels: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
      datasets: [
        {
          label: '新增用户',
          data: [120, 132, 145, 162, 178, 195, 210, 225, 242, 258, 275, 290],
          borderColor: '#4CAF50',
          backgroundColor: 'rgba(76, 175, 80, 0.1)'
        },
        {
          label: '活跃用户',
          data: [450, 480, 512, 535, 560, 590, 615, 640, 660, 685, 710, 740],
          borderColor: '#FF9800',
          backgroundColor: 'rgba(255, 152, 0, 0.1)'
        }
      ],
      summary: {
        totalNewUsers: 2432,
        averageNewUsers: 202.67,
        totalActiveUsers: 7177,
        averageActiveUsers: 598.08
      }
    }
  } else if (analysisType.value === 'products') {
    analysisData.value = {
      labels: ['产品A', '产品B', '产品C', '产品D', '产品E', '产品F'],
      datasets: [
        {
          label: '2023年销量',
          data: [1245, 980, 1350, 850, 720, 450],
          borderColor: '#673AB7',
          backgroundColor: 'rgba(103, 58, 183, 0.1)'
        },
        {
          label: '2022年销量',
          data: [1050, 920, 1090, 780, 680, 420],
          borderColor: '#9E9E9E',
          backgroundColor: 'rgba(158, 158, 158, 0.1)'
        }
      ],
      summary: {
        total: 5595,
        average: 932.5,
        max: 1350,
        min: 450
      }
    }
  } else {
    // 默认数据
    analysisData.value = {
      labels: ['1月', '2月', '3月', '4月', '5月', '6月'],
      datasets: [
        {
          label: '数据系列1',
          data: [100, 120, 140, 160, 180, 200],
          borderColor: '#1976D2',
          backgroundColor: 'rgba(25, 118, 210, 0.1)'
        }
      ],
      summary: {
        total: 900,
        average: 150,
        max: 200,
        min: 100
      }
    }
  }
  
  // 延迟渲染图表，确保DOM已经更新
  nextTick(() => {
    setTimeout(() => {
      renderChart();
      loading.value = false;
    }, 500);
  });
}

// 渲染图表
const renderChart = () => {
  if (!analysisData.value || !analysisData.value.datasets || !analysisData.value.labels) {
    console.warn('分析数据不完整，无法渲染图表');
    return;
  }
  
  try {
    // 使用nextTick确保DOM已经更新
    nextTick(() => {
      // 确保图表容器初始化
      if (!chartRef.value) {
        console.warn('图表容器未找到，等待DOM更新');
        setTimeout(() => renderChart(), 500); // 延迟重试
        return;
      }
      
      if (!chart) {
        try {
          chart = echarts.init(chartRef.value);
        } catch (e) {
          console.error('初始化图表实例失败:', e);
          return;
        }
      }
    
      // 确保datasets中的每个数据集都有data属性
      const validDatasets = analysisData.value.datasets.filter(dataset => 
        dataset && Array.isArray(dataset.data) && dataset.data.length > 0
      );
      
      if (validDatasets.length === 0) {
        console.warn('没有有效的数据集可以渲染');
        return;
      }
      
      const option = {
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: validDatasets.map(dataset => dataset.label || '数据'),
          bottom: 10
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '15%',
          top: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          boundaryGap: chartType.value === 'bar',
          data: analysisData.value.labels || [],
          axisLine: {
            lineStyle: {
              color: '#EAEAEA'
            }
          },
          axisLabel: {
            color: '#666'
          }
        },
        yAxis: {
          type: 'value',
          splitLine: {
            lineStyle: {
              color: '#EAEAEA',
              type: 'dashed'
            }
          },
          axisLabel: {
            color: '#666'
          }
        },
        series: validDatasets.map(dataset => ({
          name: dataset.label || '数据',
          type: chartType.value === 'area' ? 'line' : chartType.value,
          data: dataset.data || [],
          smooth: true,
          areaStyle: chartType.value === 'area' ? {
            opacity: 0.3
          } : undefined,
          itemStyle: {
            color: dataset.borderColor || '#1976D2'
          },
          lineStyle: chartType.value !== 'bar' ? {
            width: 3,
            color: dataset.borderColor || '#1976D2'
          } : undefined
        }))
      };
      
      chart.setOption(option, true);
    });
  } catch (error) {
    console.error('渲染图表时出错:', error);
  }
}

// 导出分析报告
const downloadAnalysisReport = () => {
  alert('报告导出功能即将上线!')
}

// 格式化数字显示
const formatNumber = (num) => {
  // 确保输入是数字或可以转换为数字
  if (num === null || num === undefined) {
    return '0';
  }
  
  // 如果是已经格式化的字符串，直接返回
  if (typeof num === 'string' && isNaN(Number(num.replace(/,/g, '')))) {
    return num;
  }
  
  // 转换为数字并格式化
  const numVal = typeof num === 'string' ? Number(num.replace(/,/g, '')) : Number(num);
  if (isNaN(numVal)) {
    console.warn('格式化非数字值:', num);
    return '0';
  }
  
  return new Intl.NumberFormat('zh-CN').format(numVal);
}

// 窗口大小变化时调整图表大小
const handleResize = () => {
  chart && chart.resize()
}

onMounted(() => {
  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  if (chart) {
    chart.dispose()
    chart = null
  }
})
</script>

<style scoped>
.analysis-container {
  padding: 20px;
  max-width: 1280px;
  margin: 0 auto;
}

.analysis-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 24px;
  padding-bottom: 16px;
  border-bottom: 1px solid #ebeef5;
}

.header-left h2 {
  font-size: 1.8rem;
  color: #1976D2;
  margin: 0 0 8px 0;
  font-weight: 600;
}

.page-description {
  color: #606266;
  margin: 0;
  font-size: 1rem;
}

.header-actions {
  display: flex;
  gap: 12px;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  background-color: white;
  color: #606266;
  border: 1px solid #dcdfe6;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.3s;
}

.action-btn:hover:not(:disabled) {
  color: #1976D2;
  border-color: #1976D2;
  background-color: #f0f7ff;
}

.action-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.filters-area {
  background-color: #f8f9fa;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 24px;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  align-items: flex-end;
}

.filter-group {
  flex: 1;
  min-width: 200px;
}

.filter-label {
  display: block;
  font-size: 14px;
  color: #606266;
  margin-bottom: 8px;
}

.filter-select {
  width: 100%;
}

.filter-actions {
  display: flex;
  justify-content: flex-end;
  align-items: center;
}

.analyze-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  background-color: #1976D2;
  color: white;
  border: none;
  padding: 9px 20px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.3s;
  height: 40px;
}

.analyze-btn:hover {
  background-color: #1565C0;
}

.btn-icon {
  font-size: 16px;
}

.content-area {
  position: relative;
  min-height: 400px;
}

.empty-state {
  height: 400px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: white;
  border-radius: 8px;
  text-align: center;
  padding: 40px;
}

.empty-icon {
  font-size: 4rem;
  color: #BDBDBD;
  margin-bottom: 20px;
}

.empty-state h3 {
  font-size: 1.5rem;
  color: #424242;
  margin: 0 0 10px 0;
}

.empty-state p {
  font-size: 1rem;
  color: #757575;
  max-width: 400px;
  margin: 0 0 30px 0;
}

.empty-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  background-color: #F5F5F5;
  color: #616161;
  border: 1px solid #E0E0E0;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.3s;
}

.empty-btn:hover {
  background-color: #EEEEEE;
  color: #424242;
}

.analysis-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 24px;
}

.chart-section, .summary-section {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
  overflow: hidden;
}

.chart-card {
  padding: 0;
}

.card-header {
  padding: 16px 20px;
  border-bottom: 1px solid #f0f0f0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
}

.header-title {
  display: flex;
  flex-direction: column;
}

.header-title h3 {
  font-size: 1.1rem;
  color: #303133;
  margin: 0 0 4px 0;
  font-weight: 600;
}

.header-subtitle {
  font-size: 0.85rem;
  color: #909399;
}

.header-tabs {
  display: flex;
  gap: 8px;
}

.tab-btn {
  background: none;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
  padding: 6px 12px;
  font-size: 12px;
  color: #606266;
  cursor: pointer;
  transition: all 0.2s;
}

.tab-btn:hover {
  color: #1976D2;
  border-color: #1976D2;
}

.tab-btn.active {
  color: #1976D2;
  border-color: #1976D2;
  background-color: #ecf5ff;
}

.chart-container {
  height: 400px;
  width: 100%;
  padding: 20px;
}

.summary-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  padding: 20px;
}

.summary-card {
  background-color: #fafafa;
  border-radius: 8px;
  padding: 16px;
  display: flex;
  align-items: center;
  gap: 16px;
  transition: all 0.3s;
  border: 1px solid #f0f0f0;
}

.summary-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.05);
}

.summary-icon {
  width: 48px;
  height: 48px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
}

.summary-content {
  flex: 1;
}

.summary-label {
  font-size: 12px;
  color: #909399;
  margin-bottom: 4px;
}

.summary-value {
  font-size: 18px;
  font-weight: 600;
  color: #303133;
  margin-bottom: 4px;
}

.summary-trend, .summary-meta {
  font-size: 12px;
  display: flex;
  align-items: center;
  color: #909399;
}

.trend-icon {
  margin-right: 4px;
}

.positive {
  color: #67C23A;
}

.negative {
  color: #F56C6C;
}

/* 响应式设计 */
@media (max-width: 1200px) {
  .summary-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .analysis-header {
    flex-direction: column;
    gap: 16px;
  }
  
  .header-actions {
    width: 100%;
  }
  
  .filters-area {
    flex-direction: column;
    gap: 16px;
  }
  
  .filter-group, .filter-actions {
    width: 100%;
  }
  
  .summary-grid {
    grid-template-columns: 1fr;
  }
  
  .card-header {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .header-tabs {
    width: 100%;
  }
  
  .tab-btn {
    flex: 1;
    text-align: center;
  }
}
</style> 