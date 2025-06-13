# 数据分析平台

一个现代化的数据分析和可视化平台，提供数据仪表盘、数据分析、报表管理和数据大屏等功能。

## ✨ 主要特性

- 🎯 **数据仪表盘** - 实时数据监控和关键指标展示
- 📊 **数据分析** - 多维度数据分析和可视化
- 📋 **报表管理** - 报表创建、编辑和导出功能
- 🖥️ **数据大屏** - 全屏数据可视化展示
- 👤 **用户管理** - 用户认证、权限管理和个人设置
- 🔍 **全局搜索** - 智能搜索功能，支持多类型内容检索
- 🌐 **国际化** - 多语言支持
- 🎨 **现代化UI** - 响应式设计，支持深色/浅色主题

## 🛠️ 技术栈

### 前端
- **框架**: Vue 3 + Composition API
- **构建工具**: Vite
- **UI组件库**: Element Plus
- **状态管理**: Pinia
- **路由**: Vue Router 4
- **图表库**: ECharts 5
- **HTTP客户端**: Axios
- **国际化**: Vue I18n
- **样式**: CSS3 + 现代化设计

### 后端
- **框架**: Flask (Python)
- **数据库**: MySQL
- **ORM**: SQLAlchemy
- **认证**: JWT (Flask-JWT-Extended)
- **跨域**: Flask-CORS
- **数据处理**: Pandas, NumPy
- **机器学习**: Scikit-learn
- **可视化**: Matplotlib

## 📁 项目结构

```
data-analysis-platform/
├── frontend/                 # 前端项目
│   ├── src/
│   │   ├── views/            # 页面组件
│   │   ├── components/       # 公共组件
│   │   ├── router/           # 路由配置
│   │   ├── stores/           # Pinia状态管理
│   │   ├── assets/           # 静态资源
│   │   └── i18n/             # 国际化配置
│   ├── package.json
│   └── vite.config.js
├── backend/                  # 后端项目
│   ├── app.py               # Flask应用主文件
│   ├── models.py            # 数据模型
│   ├── config.py            # 配置文件
│   ├── init_db.py           # 数据库初始化
│   └── requirements.txt     # Python依赖
├── config.json              # 项目配置
└── README.md               # 项目文档
```

## 🚀 快速开始

### 环境要求

- Node.js >= 16.0.0
- Python >= 3.8
- MySQL >= 5.7

### 安装步骤

1. **克隆项目**
```bash
git clone <repository-url>
cd data-analysis-platform
```

2. **后端设置**
```bash
cd backend

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

3. **数据库配置**
```bash
# 创建 .env 文件
cp .env.example .env

# 编辑 .env 文件，配置数据库连接
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=data_analysis
JWT_SECRET_KEY=your_secret_key
```

4. **初始化数据库**
```bash
python init_db.py
```

5. **前端设置**
```bash
cd ../frontend

# 安装依赖
npm install
```

### 运行项目

1. **启动后端服务**
```bash
cd backend
python app.py
```
后端服务将在 http://127.0.0.1:5000 启动

2. **启动前端服务**
```bash
cd frontend
npm run serve
```
前端服务将在 http://localhost:5173 启动

## 📊 功能模块

### 1. 数据仪表盘
- 关键业务指标展示
- 销售趋势分析
- 用户分布统计
- 产品销售对比
- 实时数据更新

### 2. 数据分析
- 多维度数据分析
- 可视化图表展示
- 时间序列分析
- 数据筛选和过滤
- 分析结果导出

### 3. 报表管理
- 报表创建和编辑
- 多种报表类型支持
- 报表预览和下载
- 报表状态管理
- 搜索和筛选功能

### 4. 数据大屏
- 全屏数据展示
- 实时数据更新
- 地图可视化
- 动态效果展示
- 自适应布局

### 5. 用户系统
- 用户注册和登录
- JWT身份认证
- 个人资料管理
- 系统设置
- 权限控制

## 🔧 配置说明

### 环境变量

在 `backend/.env` 文件中配置以下环境变量：

```env
# 数据库配置
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=data_analysis

# JWT配置
JWT_SECRET_KEY=your_secret_key

# 其他配置
FLASK_ENV=development
```

### 前端代理配置

前端开发服务器已配置代理，将 `/api` 请求转发到后端服务：

```javascript
// vite.config.js
server: {
  proxy: {
    '/api': {
      target: 'http://127.0.0.1:5000',
      changeOrigin: true
    }
  }
}
```

## 📡 API接口

### 认证接口
- `POST /api/login` - 用户登录
- `POST /api/register` - 用户注册
- `GET /api/profile` - 获取用户信息

### 数据接口
- `GET /api/dashboard` - 获取仪表盘数据
- `GET /api/analysis` - 获取分析数据
- `GET /api/dataScreen` - 获取大屏数据
- `GET /api/reports` - 获取报表列表

### 搜索接口
- `GET /api/search` - 全局搜索

## 🏗️ 开发指南

### 前端开发

1. **组件开发**
   - 使用 Vue 3 Composition API
   - 遵循 Element Plus 设计规范
   - 组件命名采用 PascalCase

2. **状态管理**
   - 使用 Pinia 进行状态管理
   - 按功能模块划分 store

3. **样式规范**
   - 使用 CSS3 现代特性
   - 支持响应式设计
   - 遵循 BEM 命名规范

### 后端开发

1. **API设计**
   - RESTful API 设计原则
   - 统一的响应格式
   - 完善的错误处理

2. **数据库设计**
   - 使用 SQLAlchemy ORM
   - 遵循数据库设计规范
   - 合理的索引设计

## 🚀 部署指南

### 生产环境部署

1. **后端部署**
```bash
# 使用 Gunicorn 部署
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

2. **前端部署**
```bash
# 构建生产版本
npm run build

# 部署到 Web 服务器
# 将 dist 目录内容部署到 Nginx 或 Apache
```

3. **数据库配置**
   - 配置生产环境数据库
   - 设置数据库连接池
   - 配置数据备份策略

## 🤝 贡献指南

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 📞 联系方式

如有问题或建议，请通过以下方式联系：

- 项目地址: [GitHub Repository]
- 问题反馈: [GitHub Issues]

---

**数据分析平台** - 让数据分析更简单、更高效！
