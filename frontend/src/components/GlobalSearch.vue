<template>
  <div class="global-search">
    <!-- 搜索输入框 -->
    <div class="search-container" :class="{ 'search-active': isSearchActive }">
      <div class="search-input-wrapper">
        <div class="search-icon">
          <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" 
                  stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <input
          ref="searchInput"
          type="text"
          placeholder="搜索报表、分析、用户..."
          v-model="searchQuery"
          @input="handleSearchInput"
          @focus="handleSearchFocus"
          @blur="handleSearchBlur"
          @keydown.enter="performSearch"
          @keydown.escape="clearSearch"
          @keydown.down="navigateSuggestions(1)"
          @keydown.up="navigateSuggestions(-1)"
          class="search-input"
        >
        <div class="search-actions">
          <button v-if="searchQuery" @click="clearSearch" class="clear-btn">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M6 6l12 12M6 18L18 6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
          </button>
          <button @click="performSearch" class="search-btn" :disabled="!searchQuery.trim()">
            搜索
          </button>
        </div>
      </div>
      
      <!-- 搜索建议下拉框 -->
      <div v-if="showSuggestions && suggestions.length > 0" class="suggestions-dropdown">
        <div class="suggestions-header">
          <span>搜索建议</span>
        </div>
        <div class="suggestions-list">
          <div
            v-for="(suggestion, index) in suggestions"
            :key="index"
            :class="['suggestion-item', { 'suggestion-active': index === activeSuggestionIndex }]"
            @click="selectSuggestion(suggestion)"
            @mouseenter="activeSuggestionIndex = index"
          >
            <div class="suggestion-icon">
              <svg v-if="suggestion.type === 'report'" viewBox="0 0 24 24" fill="none">
                <path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" 
                      stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <svg v-else-if="suggestion.type === 'analysis'" viewBox="0 0 24 24" fill="none">
                <path d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" 
                      stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <svg v-else viewBox="0 0 24 24" fill="none">
                <path d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" 
                      stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <div class="suggestion-content">
              <div class="suggestion-text">{{ suggestion.text }}</div>
              <div class="suggestion-category">{{ suggestion.category }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 搜索结果模态框 -->
    <div v-if="showResults" class="search-results-modal" @click="closeResults">
      <div class="search-results-container" @click.stop>
        <div class="search-results-header">
          <h3>搜索结果</h3>
          <div class="search-meta">
            <span>关键词: "{{ lastSearchQuery }}"</span>
            <span>共找到 {{ searchResults.total }} 个结果</span>
          </div>
          <button @click="closeResults" class="close-btn">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M6 6l12 12M6 18L18 6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
          </button>
        </div>
        
        <div class="search-results-content">
          <!-- 报表结果 -->
          <div v-if="searchResults.results.reports.length > 0" class="result-section">
            <h4>
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" 
                      stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              报表 ({{ searchResults.results.reports.length }})
            </h4>
            <div class="result-list">
              <div v-for="report in searchResults.results.reports" :key="report.id" class="result-item">
                <div class="result-content">
                  <h5>{{ report.title }}</h5>
                  <p>{{ report.description || '暂无描述' }}</p>
                  <div class="result-meta">
                    <span class="result-type">{{ report.type }}</span>
                    <span class="result-status" :class="'status-' + report.status">{{ report.status }}</span>
                    <span class="result-date">{{ report.created_at }}</span>
                  </div>
                </div>
                <div class="result-actions">
                  <button @click="navigateToResult(report.url)" class="view-btn">查看</button>
                </div>
              </div>
            </div>
          </div>

          <!-- 分析结果 -->
          <div v-if="searchResults.results.analysis.length > 0" class="result-section">
            <h4>
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" 
                      stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              分析 ({{ searchResults.results.analysis.length }})
            </h4>
            <div class="result-list">
              <div v-for="analysis in searchResults.results.analysis" :key="analysis.id" class="result-item">
                <div class="result-content">
                  <h5>{{ analysis.name }}</h5>
                  <p>{{ analysis.description || '暂无描述' }}</p>
                  <div class="result-meta">
                    <span class="result-type">{{ analysis.type }}</span>
                    <span class="result-date">{{ analysis.created_at }}</span>
                  </div>
                </div>
                <div class="result-actions">
                  <button @click="navigateToResult(analysis.url)" class="view-btn">查看</button>
                </div>
              </div>
            </div>
          </div>

          <!-- 用户结果 -->
          <div v-if="searchResults.results.users.length > 0" class="result-section">
            <h4>
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M15 19.128a9.38 9.38 0 002.625.372 9.337 9.337 0 004.121-.952 4.125 4.125 0 00-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 018.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0111.964-3.07M12 6.375a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zm8.25 2.25a2.625 2.625 0 11-5.25 0 2.625 2.625 0 015.25 0z" 
                      stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              用户 ({{ searchResults.results.users.length }})
            </h4>
            <div class="result-list">
              <div v-for="user in searchResults.results.users" :key="user.id" class="result-item">
                <div class="result-content">
                  <h5>{{ user.username }}</h5>
                  <p>{{ user.email }}</p>
                  <div class="result-meta">
                    <span class="result-type">{{ user.role }}</span>
                    <span class="result-date">{{ user.created_at }}</span>
                  </div>
                </div>
                <div class="result-actions">
                  <button @click="navigateToResult(user.url)" class="view-btn">查看</button>
                </div>
              </div>
            </div>
          </div>

          <!-- 无结果 -->
          <div v-if="searchResults.total === 0" class="no-results">
            <div class="no-results-icon">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" 
                      stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <h4>未找到相关结果</h4>
            <p>尝试使用不同的关键词或检查拼写</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, watch, nextTick } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()

// 响应式数据
const searchQuery = ref('')
const lastSearchQuery = ref('')
const isSearchActive = ref(false)
const showSuggestions = ref(false)
const showResults = ref(false)
const suggestions = ref([])
const activeSuggestionIndex = ref(-1)
const searchInput = ref(null)

const searchResults = reactive({
  total: 0,
  results: {
    reports: [],
    users: [],
    analysis: [],
    data_sources: []
  }
})

// 防抖定时器
let suggestionTimer = null

// 监听搜索输入
const handleSearchInput = () => {
  if (suggestionTimer) {
    clearTimeout(suggestionTimer)
  }
  
  if (searchQuery.value.trim().length >= 2) {
    suggestionTimer = setTimeout(() => {
      fetchSuggestions()
    }, 300)
  } else {
    suggestions.value = []
    showSuggestions.value = false
  }
}

// 获取搜索建议
const fetchSuggestions = async () => {
  try {
    const response = await axios.get('/search/suggestions', {
      params: { q: searchQuery.value.trim(), limit: 5 }
    })
    suggestions.value = response.data.suggestions
    showSuggestions.value = suggestions.value.length > 0
    activeSuggestionIndex.value = -1
  } catch (error) {
    console.error('获取搜索建议失败:', error)
    suggestions.value = []
    showSuggestions.value = false
  }
}

// 处理搜索框焦点
const handleSearchFocus = () => {
  isSearchActive.value = true
  if (searchQuery.value.trim().length >= 2 && suggestions.value.length > 0) {
    showSuggestions.value = true
  }
}

const handleSearchBlur = () => {
  // 延迟隐藏建议，以便点击建议项
  setTimeout(() => {
    isSearchActive.value = false
    showSuggestions.value = false
  }, 200)
}

// 导航建议项
const navigateSuggestions = (direction) => {
  if (!showSuggestions.value || suggestions.value.length === 0) return
  
  activeSuggestionIndex.value += direction
  
  if (activeSuggestionIndex.value < 0) {
    activeSuggestionIndex.value = suggestions.value.length - 1
  } else if (activeSuggestionIndex.value >= suggestions.value.length) {
    activeSuggestionIndex.value = 0
  }
}

// 选择建议项
const selectSuggestion = (suggestion) => {
  searchQuery.value = suggestion.text
  showSuggestions.value = false
  performSearch()
}

// 执行搜索
const performSearch = async () => {
  const query = searchQuery.value.trim()
  if (!query) return
  
  lastSearchQuery.value = query
  showSuggestions.value = false
  
  try {
    const response = await axios.get('/search', {
      params: { q: query, type: 'all' }
    })
    
    Object.assign(searchResults, response.data)
    showResults.value = true
  } catch (error) {
    console.error('搜索失败:', error)
    // 可以显示错误提示
  }
}

// 清空搜索
const clearSearch = () => {
  searchQuery.value = ''
  suggestions.value = []
  showSuggestions.value = false
  searchInput.value?.focus()
}

// 关闭搜索结果
const closeResults = () => {
  showResults.value = false
}

// 导航到结果页面
const navigateToResult = (url) => {
  closeResults()
  router.push(url)
}

// 暴露方法给父组件
defineExpose({
  focus: () => {
    searchInput.value?.focus()
  },
  clear: clearSearch
})
</script>
