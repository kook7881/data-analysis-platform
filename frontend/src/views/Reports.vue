<template>
  <div class="reports-container">
    <!-- 背景装饰 -->
    <div class="bg-decoration">
      <div class="decoration-circle circle-1"></div>
      <div class="decoration-circle circle-2"></div>
    </div>

    <!-- 页面头部 -->
    <div class="page-header glass-card">
      <div class="header-content">
        <div class="header-title">
          <div class="title-icon">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M9 12h3.75M9 15h3.75M9 18h3.75m3 .75H18a2.25 2.25 0 002.25-2.25V6.108c0-1.135-.845-2.098-1.976-2.192a48.424 48.424 0 00-1.123-.08m-5.801 0c-.065.21-.1.433-.1.664 0 .414.336.75.75.75h4.5a.75.75 0 00.75-.75 2.25 2.25 0 00-.1-.664m-5.8 0A2.251 2.251 0 0113.5 2.25H15c1.012 0 1.867.668 2.15 1.586m-5.8 0c-.376.023-.75.05-1.124.08C9.095 4.01 8.25 4.973 8.25 6.108V8.25m0 0H4.875c-.621 0-1.125.504-1.125 1.125v11.25c0 .621.504 1.125 1.125 1.125h9.75c.621 0 1.125-.504 1.125-1.125V9.375c0-.621-.504-1.125-1.125-1.125H8.25zM6.75 12h.008v.008H6.75V12zm0 3h.008v.008H6.75V15zm0 3h.008v.008H6.75V18z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <div class="title-text">
            <h1>报表管理</h1>
            <p>管理和查看您的数据报表</p>
          </div>
        </div>

        <div class="header-actions">
          <div class="search-container">
            <div class="search-icon">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <input
              type="text"
              placeholder="搜索报表..."
              v-model="searchQuery"
              class="search-input"
            >
          </div>

          <button class="action-btn refresh-btn" @click="refreshList">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0 3.181 3.183a8.25 8.25 0 0 0 13.803-3.7M4.031 9.865a8.25 8.25 0 0 1 13.803-3.7l3.181 3.182m0-4.991v4.99" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span>刷新</span>
          </button>

          <button class="action-btn create-btn">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 4.5v15m7.5-7.5h-15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span>新建报表</span>
          </button>
        </div>
      </div>
    </div>

    <!-- 内容区域 -->
    <div class="content-area">
      <!-- 加载状态 -->
      <div v-if="loading" class="loading-overlay">
        <div class="loading-container">
          <div class="loading-spinner"></div>
          <p class="loading-text">正在加载报表数据...</p>
        </div>
      </div>

      <!-- 空状态 -->
      <div v-else-if="filteredReports.length === 0" class="empty-state glass-card">
        <div class="empty-content">
          <div class="empty-icon">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <h3>暂无报表数据</h3>
          <p>{{ searchQuery ? '没有找到匹配的报表' : '还没有创建任何报表' }}</p>
          <button class="btn btn-primary" v-if="!searchQuery">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 4.5v15m7.5-7.5h-15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span>创建第一个报表</span>
          </button>
        </div>
      </div>

      <!-- 报表列表 -->
      <div v-else class="reports-grid">
        <div
          class="report-card glass-card hover-lift"
          v-for="(report, index) in filteredReports"
          :key="report.id"
          :style="{ animationDelay: `${index * 0.1}s` }"
        >
          <div class="card-header">
            <div class="report-type-icon" :class="getTypeClass(report.type)">
              <svg v-if="report.type === '销售报表'" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.25 18.75a60.07 60.07 0 0115.797 2.101c.727.198 1.453-.342 1.453-1.096V18.75M3.75 4.5v.75A.75.75 0 013 6h-.75m0 0v-.375c0-.621.504-1.125 1.125-1.125H6m-3.75 0h3.75m0 0v.375c0 .621-.504 1.125-1.125 1.125H3.75M6 6v6h.75m0 0v3.75c0 .621.504 1.125 1.125 1.125h9.75c.621 0 1.125-.504 1.125-1.125V12.75m0 0h.375c.621 0 1.125-.504 1.125-1.125V9.75c0-.621-.504-1.125-1.125-1.125h-.375m0 3.75h.375c.621 0 1.125-.504 1.125-1.125V9.75c0-.621-.504-1.125-1.125-1.125H15m1.5 1.5v.75A.75.75 0 0115 12h-.75m-1.5-1.5h.75A.75.75 0 0115 9h.75m-1.5 1.5v.75A.75.75 0 0112 12h-.75m-1.5-1.5h.75A.75.75 0 0112 9h.75m-1.5 1.5v.75c0 .414.336.75.75.75H12m-1.5-1.5H9.75A.75.75 0 009 10.5v-.75m1.5 0h.75c.414 0 .75.336.75.75v.75H12m-1.5-1.5v.75c0 .414.336.75.75.75H12m0-1.5v.75c0 .414.336.75.75.75h.75m-1.5-1.5h.75c.414 0 .75.336.75.75v.75h.75" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <svg v-else-if="report.type === '用户报表'" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M15 19.128a9.38 9.38 0 002.625.372 9.337 9.337 0 004.121-.952 4.125 4.125 0 00-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 018.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0111.964-3.07M12 6.375a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zm8.25 2.25a2.625 2.625 0 11-5.25 0 2.625 2.625 0 015.25 0z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <svg v-else-if="report.type === '产品报表'" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M20.25 7.5l-.625 10.632a2.25 2.25 0 01-2.247 2.118H6.622a2.25 2.25 0 01-2.247-2.118L3.75 7.5M10 11.25h4M3.375 7.5h17.25c.621 0 1.125-.504 1.125-1.125v-1.5c0-.621-.504-1.125-1.125-1.125H3.375c-.621 0-1.125.504-1.125 1.125v1.5c0 .621.504 1.125 1.125 1.125z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <svg v-else viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 013 19.875v-6.75zM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V8.625zM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V4.125z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>

            <div class="status-badge" :class="getStatusClass(report.status)">
              <div class="status-dot"></div>
              <span>{{ report.status }}</span>
            </div>
          </div>

          <div class="card-content">
            <h3 class="report-title">{{ report.name }}</h3>

            <div class="report-meta">
              <div class="meta-row">
                <div class="meta-item">
                  <svg class="meta-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M9.568 3H5.25A2.25 2.25 0 003 5.25v4.318c0 .597.237 1.17.659 1.591l9.581 9.581c.699.699 1.78.872 2.607.33a18.095 18.095 0 005.223-5.223c.542-.827.369-1.908-.33-2.607L11.16 3.66A2.25 2.25 0 009.568 3z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M6 6h.008v.008H6V6z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <span>{{ report.type }}</span>
                </div>

                <div class="meta-item">
                  <svg class="meta-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5a2.25 2.25 0 002.25-2.25m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5a2.25 2.25 0 012.25 2.25v7.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <span>{{ report.created_at }}</span>
                </div>
              </div>
            </div>
          </div>

          <div class="card-actions">
            <button class="card-btn view-btn" @click="viewReport(report)" title="查看详情">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>

            <button class="card-btn download-btn" @click="downloadReport(report)" title="下载报表">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5M16.5 12L12 16.5m0 0L7.5 12m4.5 4.5V3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>

            <button class="card-btn delete-btn" @click="confirmDelete(report)" title="删除报表">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- 报表详情模态框 -->
    <transition name="modal">
      <div v-if="showDetail" class="modal-overlay" @click="closeDetail">
        <div class="modal-container glass-card" @click.stop>
          <div class="modal-header">
            <div class="modal-title">
              <div class="title-icon" :class="getTypeClass(currentReport?.type)">
                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M9 12h3.75M9 15h3.75M9 18h3.75m3 .75H18a2.25 2.25 0 002.25-2.25V6.108c0-1.135-.845-2.098-1.976-2.192a48.424 48.424 0 00-1.123-.08m-5.801 0c-.065.21-.1.433-.1.664 0 .414.336.75.75.75h4.5a.75.75 0 00.75-.75 2.25 2.25 0 00-.1-.664m-5.8 0A2.251 2.251 0 0113.5 2.25H15c1.012 0 1.867.668 2.15 1.586m-5.8 0c-.376.023-.75.05-1.124.08C9.095 4.01 8.25 4.973 8.25 6.108V8.25m0 0H4.875c-.621 0-1.125.504-1.125 1.125v11.25c0 .621.504 1.125 1.125 1.125h9.75c.621 0 1.125-.504 1.125-1.125V9.375c0-.621-.504-1.125-1.125-1.125H8.25zM6.75 12h.008v.008H6.75V12zm0 3h.008v.008H6.75V15zm0 3h.008v.008H6.75V18z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </div>
              <div class="title-content">
                <h3>{{ currentReport?.name }}</h3>
                <div class="status-badge" :class="getStatusClass(currentReport?.status)">
                  <div class="status-dot"></div>
                  <span>{{ currentReport?.status }}</span>
                </div>
              </div>
            </div>

            <button class="close-btn" @click="closeDetail">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M6 18L18 6M6 6l12 12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>
          </div>

          <div class="modal-body">
            <!-- 统计信息 -->
            <div class="stats-grid">
              <div class="stat-card">
                <div class="stat-icon type-icon" :class="getTypeClass(currentReport?.type)">
                  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M9.568 3H5.25A2.25 2.25 0 003 5.25v4.318c0 .597.237 1.17.659 1.591l9.581 9.581c.699.699 1.78.872 2.607.33a18.095 18.095 0 005.223-5.223c.542-.827.369-1.908-.33-2.607L11.16 3.66A2.25 2.25 0 009.568 3z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </div>
                <div class="stat-content">
                  <div class="stat-label">报表类型</div>
                  <div class="stat-value">{{ currentReport?.type }}</div>
                </div>
              </div>

              <div class="stat-card">
                <div class="stat-icon time-icon">
                  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </div>
                <div class="stat-content">
                  <div class="stat-label">创建时间</div>
                  <div class="stat-value">{{ currentReport?.created_at }}</div>
                </div>
              </div>

              <div class="stat-card">
                <div class="stat-icon data-icon">
                  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 013 19.875v-6.75zM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V8.625zM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V4.125z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </div>
                <div class="stat-content">
                  <div class="stat-label">数据量</div>
                  <div class="stat-value">1,245 条</div>
                </div>
              </div>
            </div>

            <!-- 图表预览区域 -->
            <div class="chart-preview glass-card">
              <div class="preview-header">
                <h4>数据预览</h4>
                <div class="preview-actions">
                  <button class="preview-btn">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M3.75 3v11.25A2.25 2.25 0 006 16.5h2.25M3.75 3h-1.5m1.5 0h16.5m0 0h1.5m-1.5 0v11.25A2.25 2.25 0 0118 16.5h-2.25m-7.5 0h7.5m-7.5 0l-1 3m8.5-3l1 3m0 0l.5 1.5m-.5-1.5h-9.5m0 0l-.5 1.5M9 11.25v1.5M12 9v3.75m3-6v6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                  </button>
                  <button class="preview-btn">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0 3.181 3.183a8.25 8.25 0 0 0 13.803-3.7M4.031 9.865a8.25 8.25 0 0 1 13.803-3.7l3.181 3.182m0-4.991v4.99" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                  </button>
                </div>
              </div>

              <div class="preview-content">
                <div class="chart-placeholder">
                  <div class="chart-icon">
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M2.25 18L9 11.25l4.306 4.307a11.95 11.95 0 015.814-5.519l2.74-1.22m0 0l-5.94-2.28m5.94 2.28l-2.28 5.941" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                  </div>
                  <h5>图表预览</h5>
                  <p>在实际应用中，这里将显示动态图表和数据可视化内容</p>
                </div>
              </div>
            </div>

            <!-- 详细信息 -->
            <div class="detail-info">
              <h4>报表详情</h4>
              <div class="info-grid">
                <div class="info-item">
                  <span class="info-label">时间范围</span>
                  <span class="info-value">2023年1月 - 6月</span>
                </div>
                <div class="info-item">
                  <span class="info-label">更新频率</span>
                  <span class="info-value">每日更新</span>
                </div>
                <div class="info-item">
                  <span class="info-label">数据源</span>
                  <span class="info-value">主数据库</span>
                </div>
                <div class="info-item">
                  <span class="info-label">文件大小</span>
                  <span class="info-value">2.4 MB</span>
                </div>
              </div>
            </div>
          </div>

          <div class="modal-footer">
            <button class="btn btn-secondary" @click="closeDetail">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M6 18L18 6M6 6l12 12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <span>关闭</span>
            </button>

            <button class="btn btn-primary" @click="downloadReport(currentReport)">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5M16.5 12L12 16.5m0 0L7.5 12m4.5 4.5V3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <span>下载报表</span>
            </button>
          </div>
        </div>
      </div>
    </transition>

    <!-- 删除确认对话框 -->
    <transition name="modal">
      <div v-if="showDeleteConfirm" class="modal-overlay" @click="cancelDelete">
        <div class="confirm-modal glass-card" @click.stop>
          <div class="confirm-header">
            <div class="warning-icon">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126zM12 15.75h.007v.008H12v-.008z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <div class="confirm-title">
              <h3>确认删除</h3>
              <p>此操作无法撤销</p>
            </div>
          </div>

          <div class="confirm-content">
            <p>您确定要删除报表 <strong>"{{ reportToDelete?.name }}"</strong> 吗？</p>
            <div class="warning-note">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M11.25 11.25l.041-.02a.75.75 0 011.063.852l-.708 2.836a.75.75 0 001.063.853l.041-.021M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9-3.75h.008v.008H12V8.25z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <span>删除后将无法恢复，请谨慎操作</span>
            </div>
          </div>

          <div class="confirm-actions">
            <button class="btn btn-ghost" @click="cancelDelete">
              <span>取消</span>
            </button>
            <button class="btn btn-danger" @click="deleteReport">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <span>确认删除</span>
            </button>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'ReportsView',
  data() {
    return {
      loading: false,
      searchQuery: '',
      reports: [
        { id: 1, name: '2023年第一季度销售报告', type: '销售报表', created_at: '2023-04-01', status: '已完成' },
        { id: 2, name: '用户增长分析', type: '用户报表', created_at: '2023-04-15', status: '已完成' },
        { id: 3, name: '产品性能评估', type: '产品报表', created_at: '2023-05-01', status: '处理中' },
        { id: 4, name: '市场竞争分析', type: '市场报表', created_at: '2023-05-10', status: '草稿' },
        { id: 5, name: '2023年第二季度销售预测', type: '销售报表', created_at: '2023-05-20', status: '处理中' }
      ],
      currentReport: null,
      showDetail: false,
      showDeleteConfirm: false,
      reportToDelete: null
    };
  },
  computed: {
    filteredReports() {
      if (!this.searchQuery) return this.reports;
      
      const query = this.searchQuery.toLowerCase();
      return this.reports.filter(report => 
        report.name.toLowerCase().includes(query) || 
        report.type.toLowerCase().includes(query)
      );
    }
  },
  methods: {
    refreshList() {
      this.loading = true;
      // 模拟网络请求延迟
      setTimeout(() => {
        this.loading = false;
      }, 800);
    },
    
    viewReport(report) {
      this.currentReport = report;
      this.showDetail = true;
    },
    
    closeDetail() {
      this.showDetail = false;
      this.currentReport = null;
    },
    
    downloadReport(report) {
      alert(`开始下载报表: ${report.name}`);
    },
    
    confirmDelete(report) {
      this.reportToDelete = report;
      this.showDeleteConfirm = true;
    },
    
    cancelDelete() {
      this.showDeleteConfirm = false;
      this.reportToDelete = null;
    },
    
    deleteReport() {
      if (!this.reportToDelete) return;
      
      const index = this.reports.findIndex(r => r.id === this.reportToDelete.id);
      if (index !== -1) {
        this.reports.splice(index, 1);
        alert(`报表 "${this.reportToDelete.name}" 已删除`);
      }
      
      this.showDeleteConfirm = false;
      this.reportToDelete = null;
    },
    
    getStatusClass(status) {
      const map = {
        '已完成': 'status-success',
        '处理中': 'status-warning',
        '草稿': 'status-info'
      };
      return map[status] || 'status-default';
    },
    
    getTypeClass(type) {
      const map = {
        '销售报表': 'type-sales',
        '用户报表': 'type-users',
        '产品报表': 'type-products',
        '市场报表': 'type-market'
      };
      return map[type] || 'type-default';
    }
  },
  mounted() {
    // 模拟加载数据
    this.loading = true;
    setTimeout(() => {
      this.loading = false;
    }, 800);
  }
};
</script>

<style scoped>
/* 基础容器 */
.reports-container {
  min-height: 100vh;
  padding: var(--spacing-lg);
  position: relative;
  background: var(--bg-primary);
  max-width: 1400px;
  margin: 0 auto;
}

/* 背景装饰 */
.bg-decoration {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
}

.decoration-circle {
  position: absolute;
  border-radius: 50%;
  background: linear-gradient(135deg,
    rgba(79, 172, 254, 0.05),
    rgba(67, 233, 123, 0.05));
  animation: float 8s ease-in-out infinite;
}

.circle-1 {
  width: 300px;
  height: 300px;
  top: 20%;
  right: -150px;
  animation-delay: 0s;
}

.circle-2 {
  width: 200px;
  height: 200px;
  bottom: 30%;
  left: -100px;
  animation-delay: 4s;
}

/* 页面头部 */
.page-header {
  position: relative;
  z-index: 1;
  margin-bottom: var(--spacing-xl);
  animation: fadeInDown 0.6s ease-out;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--spacing-xl);
}

.header-title {
  display: flex;
  align-items: center;
  gap: var(--spacing-lg);
}

.title-icon {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  border-radius: var(--radius-lg);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: var(--shadow-md);
}

.title-icon svg {
  width: 28px;
  height: 28px;
}

.title-text h1 {
  font-size: 2.5rem;
  font-weight: 800;
  margin: 0 0 var(--spacing-xs) 0;
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.title-text p {
  color: var(--text-muted);
  margin: 0;
  font-size: 1.1rem;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
}

/* 搜索容器 */
.search-container {
  position: relative;
  display: flex;
  align-items: center;
}

.search-icon {
  position: absolute;
  left: var(--spacing-md);
  width: 20px;
  height: 20px;
  color: var(--text-muted);
  z-index: 2;
}

.search-input {
  width: 280px;
  height: 48px;
  padding: 0 var(--spacing-md) 0 52px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  color: var(--text-primary);
  font-size: 0.95rem;
  transition: var(--transition-normal);
}

.search-input::placeholder {
  color: var(--text-muted);
}

.search-input:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(79, 172, 254, 0.1);
  background: rgba(255, 255, 255, 0.08);
  width: 320px;
}

/* 操作按钮 */
.action-btn {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  padding: var(--spacing-md) var(--spacing-lg);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  background: rgba(255, 255, 255, 0.05);
  color: var(--text-secondary);
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: var(--transition-normal);
}

.action-btn svg {
  width: 18px;
  height: 18px;
}

.action-btn:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: var(--border-hover);
  color: var(--text-primary);
  transform: translateY(-2px);
}

.create-btn {
  background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
  border-color: var(--primary-color);
  color: white;
}

.create-btn:hover {
  background: linear-gradient(135deg, var(--primary-dark), var(--primary-color));
  box-shadow: var(--shadow-glow);
}

/* 页面特定样式覆盖 */
@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}


</style>