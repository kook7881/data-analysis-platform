<template>
  <div class="notification-center">
    <!-- 通知按钮 -->
    <div class="notification-trigger" @click="toggleNotifications">
      <button class="notification-btn" :class="{ 'has-unread': unreadCount > 0 }">
        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M14.857 17.082a23.848 23.848 0 0 0 5.25-1.878A2.25 2.25 0 0 0 21.75 13.5V8.25a9 9 0 1 0-18 0v5.25a2.25 2.25 0 0 0 1.643 2.204 23.848 23.848 0 0 0 5.25 1.878m9.164 0a23.848 23.848 0 0 1-9.164 0m9.164 0a23.848 23.848 0 0 1-.956 6.058l-.61 2.115a.75.75 0 0 1-.737.585H8.05a.75.75 0 0 1-.737-.585l-.61-2.115a23.848 23.848 0 0 1-.956-6.058" 
                stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <span v-if="unreadCount > 0" class="notification-badge">{{ unreadCount > 99 ? '99+' : unreadCount }}</span>
      </button>
    </div>

    <!-- 通知下拉面板 -->
    <div v-if="showNotifications" class="notification-dropdown" @click.stop>
      <div class="notification-header">
        <h3>通知中心</h3>
        <div class="notification-actions">
          <button v-if="unreadCount > 0" @click="markAllAsRead" class="mark-all-btn">
            全部已读
          </button>
          <button @click="closeNotifications" class="close-btn">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M6 6l12 12M6 18L18 6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
          </button>
        </div>
      </div>

      <!-- 通知过滤器 -->
      <div class="notification-filters">
        <button 
          v-for="filter in filters" 
          :key="filter.key"
          :class="['filter-btn', { 'filter-active': activeFilter === filter.key }]"
          @click="setActiveFilter(filter.key)"
        >
          {{ filter.label }}
        </button>
      </div>

      <!-- 通知列表 -->
      <div class="notification-list" ref="notificationList">
        <div v-if="loading" class="notification-loading">
          <div class="loading-spinner"></div>
          <span>加载中...</span>
        </div>

        <div v-else-if="filteredNotifications.length === 0" class="notification-empty">
          <div class="empty-icon">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M14.857 17.082a23.848 23.848 0 0 0 5.25-1.878A2.25 2.25 0 0 0 21.75 13.5V8.25a9 9 0 1 0-18 0v5.25a2.25 2.25 0 0 0 1.643 2.204 23.848 23.848 0 0 0 5.25 1.878m9.164 0a23.848 23.848 0 0 1-9.164 0m9.164 0a23.848 23.848 0 0 1-.956 6.058l-.61 2.115a.75.75 0 0 1-.737.585H8.05a.75.75 0 0 1-.737-.585l-.61-2.115a23.848 23.848 0 0 1-.956-6.058" 
                    stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <h4>暂无通知</h4>
          <p>{{ activeFilter === 'unread' ? '没有未读通知' : '没有通知消息' }}</p>
        </div>

        <div v-else class="notification-items">
          <div
            v-for="notification in filteredNotifications"
            :key="notification.id"
            :class="[
              'notification-item',
              `notification-${notification.type}`,
              { 'notification-unread': !notification.is_read },
              { 'notification-important': notification.is_important }
            ]"
            @click="handleNotificationClick(notification)"
          >
            <!-- 通知图标 -->
            <div class="notification-icon">
              <svg v-if="notification.type === 'success'" viewBox="0 0 24 24" fill="none">
                <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" 
                      stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <svg v-else-if="notification.type === 'warning'" viewBox="0 0 24 24" fill="none">
                <path d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126zM12 15.75h.007v.008H12v-.008z" 
                      stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <svg v-else-if="notification.type === 'error'" viewBox="0 0 24 24" fill="none">
                <path d="M9.75 9.75l4.5 4.5m0-4.5l-4.5 4.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" 
                      stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <svg v-else viewBox="0 0 24 24" fill="none">
                <path d="M11.25 11.25l.041-.02a.75.75 0 011.063.852l-.708 2.836a.75.75 0 001.063.853l.041-.021M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9-3.75h.008v.008H12V8.25z" 
                      stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>

            <!-- 通知内容 -->
            <div class="notification-content">
              <div class="notification-title">
                {{ notification.title }}
                <span v-if="notification.is_important" class="important-badge">重要</span>
              </div>
              <div class="notification-message">{{ notification.message }}</div>
              <div class="notification-meta">
                <span class="notification-category">{{ getCategoryLabel(notification.category) }}</span>
                <span class="notification-time">{{ formatTime(notification.created_at) }}</span>
              </div>
            </div>

            <!-- 未读指示器 -->
            <div v-if="!notification.is_read" class="unread-indicator"></div>
          </div>
        </div>

        <!-- 加载更多 -->
        <div v-if="hasMore && !loading" class="load-more">
          <button @click="loadMore" class="load-more-btn">
            加载更多
          </button>
        </div>
      </div>
    </div>

    <!-- 遮罩层 -->
    <div v-if="showNotifications" class="notification-overlay" @click="closeNotifications"></div>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted, onUnmounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()

// 响应式数据
const showNotifications = ref(false)
const loading = ref(false)
const unreadCount = ref(0)
const activeFilter = ref('all')
const notifications = ref([])
const currentPage = ref(1)
const hasMore = ref(true)
const notificationList = ref(null)

// 过滤器配置
const filters = [
  { key: 'all', label: '全部' },
  { key: 'unread', label: '未读' },
  { key: 'important', label: '重要' },
  { key: 'system', label: '系统' },
  { key: 'report', label: '报表' }
]

// 计算属性
const filteredNotifications = computed(() => {
  if (activeFilter.value === 'all') {
    return notifications.value
  } else if (activeFilter.value === 'unread') {
    return notifications.value.filter(n => !n.is_read)
  } else if (activeFilter.value === 'important') {
    return notifications.value.filter(n => n.is_important)
  } else {
    return notifications.value.filter(n => n.category === activeFilter.value)
  }
})

// 方法
const toggleNotifications = () => {
  showNotifications.value = !showNotifications.value
  if (showNotifications.value) {
    loadNotifications()
  }
}

const closeNotifications = () => {
  showNotifications.value = false
}

const setActiveFilter = (filter) => {
  activeFilter.value = filter
}

const loadNotifications = async (page = 1) => {
  if (loading.value) return
  
  loading.value = true
  try {
    const response = await axios.get('/notifications', {
      params: {
        page,
        per_page: 20,
        unread_only: activeFilter.value === 'unread'
      }
    })
    
    if (page === 1) {
      notifications.value = response.data.notifications
    } else {
      notifications.value.push(...response.data.notifications)
    }
    
    hasMore.value = response.data.has_more
    currentPage.value = page
  } catch (error) {
    console.error('加载通知失败:', error)
  } finally {
    loading.value = false
  }
}

const loadMore = () => {
  loadNotifications(currentPage.value + 1)
}

const loadUnreadCount = async () => {
  try {
    const response = await axios.get('/notifications/unread-count')
    unreadCount.value = response.data.count
  } catch (error) {
    console.error('获取未读通知数量失败:', error)
  }
}

const markAsRead = async (notificationId) => {
  try {
    await axios.post(`/notifications/${notificationId}/read`)
    
    // 更新本地状态
    const notification = notifications.value.find(n => n.id === notificationId)
    if (notification && !notification.is_read) {
      notification.is_read = true
      notification.read_at = new Date().toISOString()
      unreadCount.value = Math.max(0, unreadCount.value - 1)
    }
  } catch (error) {
    console.error('标记通知已读失败:', error)
  }
}

const markAllAsRead = async () => {
  try {
    await axios.post('/notifications/read-all')
    
    // 更新本地状态
    notifications.value.forEach(notification => {
      if (!notification.is_read) {
        notification.is_read = true
        notification.read_at = new Date().toISOString()
      }
    })
    unreadCount.value = 0
  } catch (error) {
    console.error('标记所有通知已读失败:', error)
  }
}

const handleNotificationClick = (notification) => {
  // 标记为已读
  if (!notification.is_read) {
    markAsRead(notification.id)
  }
  
  // 如果有跳转链接，则跳转
  if (notification.action_url) {
    closeNotifications()
    router.push(notification.action_url)
  }
}

const getCategoryLabel = (category) => {
  const categoryMap = {
    system: '系统',
    report: '报表',
    analysis: '分析',
    user: '用户'
  }
  return categoryMap[category] || category
}

const formatTime = (timeString) => {
  const time = new Date(timeString)
  const now = new Date()
  const diff = now - time
  
  const minutes = Math.floor(diff / 60000)
  const hours = Math.floor(diff / 3600000)
  const days = Math.floor(diff / 86400000)
  
  if (minutes < 1) return '刚刚'
  if (minutes < 60) return `${minutes}分钟前`
  if (hours < 24) return `${hours}小时前`
  if (days < 7) return `${days}天前`
  
  return time.toLocaleDateString()
}

// 监听过滤器变化
watch(activeFilter, () => {
  currentPage.value = 1
  hasMore.value = true
  loadNotifications(1)
})

// 生命周期
onMounted(() => {
  loadUnreadCount()
  
  // 定期更新未读数量
  const interval = setInterval(loadUnreadCount, 30000) // 每30秒更新一次
  
  onUnmounted(() => {
    clearInterval(interval)
  })
})

// 点击外部关闭
const handleClickOutside = (event) => {
  if (showNotifications.value && !event.target.closest('.notification-center')) {
    closeNotifications()
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>
