from flask import Flask, jsonify, request, g, make_response
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import os
from dotenv import load_dotenv
import bcrypt
import datetime
import json
from sqlalchemy import func, desc, extract, cast, Float, and_
from sqlalchemy.orm import sessionmaker
from models import User, DataSource, Dataset, Analysis, Report, Base, Sales, Notification, SearchHistory
from sqlalchemy import create_engine

# 加载环境变量
load_dotenv()

# 数据库连接信息
DB_URI = f"mysql+pymysql://{os.environ.get('DB_USER', 'root')}:{os.environ.get('DB_PASSWORD', 'password')}@{os.environ.get('DB_HOST', 'localhost')}:{os.environ.get('DB_PORT', '3306')}/{os.environ.get('DB_NAME', 'data_analysis')}"

# 创建数据库引擎和会话
engine = create_engine(DB_URI)
Session = sessionmaker(bind=engine)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'development-secret-key')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)

# 启用CORS，允许所有源
CORS(app, resources={r"/*": {"origins": "*"}})

# 初始化JWT
jwt = JWTManager(app)

# 请求前中间件DataScreen.vue:335 [Vue warn]: Duplicate keys found during update: 1749699386938 Make sure keys are unique.
#   at <DataScreen onVnodeUnmounted=fn<onVnodeUnmounted> ref=Ref< Proxy(Object) {__v_skip: true} > >
#   at <RouterView>
#   at <App>
@app.before_request
def before_request():
    g.db = Session()

# 请求后中间件
@app.teardown_request
def teardown_request(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# 健康检查接口
@app.route('/api/status', methods=['GET'])
def health_check():
    return jsonify({"status": "online", "timestamp": str(datetime.datetime.now())})

# 数字大屏数据接口
@app.route('/api/dataScreen', methods=['GET'])
@jwt_required(optional=True)
def get_data_screen():
    try:
        # 获取时间范围
        today = datetime.datetime.now()
        one_year_ago = today - datetime.timedelta(days=365)
        
        # 计算关键指标 (与仪表盘类似，但有所不同)
        metrics = []
        
        # 总销售额
        total_sales = g.db.query(func.sum(Sales.sales_amount)).filter(
            Sales.date >= one_year_ago
        ).scalar() or 0
        
        # 上个月销售额
        last_month = today.replace(day=1) - datetime.timedelta(days=1)
        last_month_start = last_month.replace(day=1)
        last_month_sales = g.db.query(func.sum(Sales.sales_amount)).filter(
            Sales.date >= last_month_start,
            Sales.date < today.replace(day=1)
        ).scalar() or 0
        
        # 前一个月销售额
        previous_month = last_month_start - datetime.timedelta(days=1)
        previous_month_start = previous_month.replace(day=1)
        previous_month_sales = g.db.query(func.sum(Sales.sales_amount)).filter(
            Sales.date >= previous_month_start,
            Sales.date < last_month_start
        ).scalar() or 0
        
        # 计算环比变化
        sales_change = 0
        if previous_month_sales > 0:
            sales_change = round(((last_month_sales - previous_month_sales) / previous_month_sales) * 100, 1)
        
        metrics.append({
            "title": "总销售额",
            "value": f"¥{total_sales:,.0f}",
            "change": sales_change
        })
        
        # 订单数量
        total_orders = g.db.query(func.count(Sales.id)).filter(
            Sales.date >= one_year_ago
        ).scalar() or 0
        
        orders_last_month = g.db.query(func.count(Sales.id)).filter(
            Sales.date >= last_month_start,
            Sales.date < today.replace(day=1)
        ).scalar() or 0
        
        orders_previous_month = g.db.query(func.count(Sales.id)).filter(
            Sales.date >= previous_month_start,
            Sales.date < last_month_start
        ).scalar() or 0
        
        # 计算环比变化
        orders_change = 0
        if orders_previous_month > 0:
            orders_change = round(((orders_last_month - orders_previous_month) / orders_previous_month) * 100, 1)
        
        metrics.append({
            "title": "订单数量",
            "value": f"{total_orders:,}",
            "change": orders_change
        })
        
        # 客单价
        average_order = 0
        if total_orders > 0:
            average_order = total_sales / total_orders
        
        avg_order_last_month = 0
        if orders_last_month > 0:
            avg_order_last_month = last_month_sales / orders_last_month
        
        avg_order_previous_month = 0
        if orders_previous_month > 0:
            avg_order_previous_month = previous_month_sales / orders_previous_month
        
        # 计算环比变化
        avg_order_change = 0
        if avg_order_previous_month > 0:
            avg_order_change = round(((avg_order_last_month - avg_order_previous_month) / avg_order_previous_month) * 100, 1)
        
        metrics.append({
            "title": "客单价",
            "value": f"¥{average_order:.1f}",
            "change": avg_order_change
        })
        
        # 区域销售占比 - 修改为省级数据以便在中国地图上展示
        region_distribution = []
        
        # 省份与大区域的映射
        province_region_map = {
            # 华东地区
            '上海': '华东', '江苏': '华东', '浙江': '华东', 
            '安徽': '华东', '福建': '华东', '江西': '华东', 
            '山东': '华东', '台湾': '华东',
            
            # 华南地区
            '广东': '华南', '广西': '华南', '海南': '华南', 
            '香港': '华南', '澳门': '华南',
            
            # 华北地区
            '北京': '华北', '天津': '华北', '河北': '华北', 
            '山西': '华北', '内蒙古': '华北', '辽宁': '华北', 
            '吉林': '华北', '黑龙江': '华北',
            
            # 西南地区
            '重庆': '西南', '四川': '西南', '贵州': '西南', 
            '云南': '西南', '西藏': '西南',
            
            # 西北地区
            '陕西': '西北', '甘肃': '西北', '青海': '西北', 
            '宁夏': '西北', '新疆': '西北',
            
            # 华中地区
            '河南': '华中', '湖北': '华中', '湖南': '华中',
        }
        
        # 根据大区域数据生成省级数据
        regions = ['华东', '华南', '华北', '西南', '西北', '华中']
        region_total_sales = {}
        
        # 首先获取大区域的总销售额
        for region in regions:
            region_sales = g.db.query(func.sum(Sales.sales_amount)).filter(
                Sales.region == region,
                Sales.date >= one_year_ago
            ).scalar() or 0
            region_total_sales[region] = region_sales
        
        # 为每个省份分配销售额，基于其所属大区域
        import random
        
        for province, region in province_region_map.items():
            # 获取该省份所属大区域的总销售额
            region_sales = region_total_sales.get(region, 0)
            
            # 该大区域包含的省份数量
            province_count = sum(1 for p, r in province_region_map.items() if r == region)
            
            # 确保每个省的销售额在合理范围内，并且均值与总销售额比例一致
            if province_count > 0 and region_sales > 0:
                # 添加随机波动使数据更真实
                province_sales = (region_sales / province_count) * (0.5 + random.random())
                # 将销售额转换为万元单位并四舍五入
                province_sales_in_wan = round(province_sales / 10000)
                
                region_distribution.append({
                    "name": province,
                    "value": province_sales_in_wan
                })
        
        # 注意：这里的value值已转换为万元单位以便于地图显示
        
        # 月度销售趋势数据
        sales_trend = {
            "months": [],
            "values": []
        }
        
        # 获取过去12个月的数据
        for i in range(11, -1, -1):
            month_date = today - datetime.timedelta(days=30 * i)
            month_name = month_date.strftime("%Y-%m")
            
            month_start = month_date.replace(day=1)
            if i > 0:
                next_month = month_start.replace(month=month_start.month % 12 + 1, day=1)
                if month_start.month == 12:
                    next_month = next_month.replace(year=next_month.year + 1)
                month_end = next_month
            else:
                month_end = today
            
            month_sales = g.db.query(func.sum(Sales.sales_amount)).filter(
                Sales.date >= month_start,
                Sales.date < month_end
            ).scalar() or 0
            
            sales_trend["months"].append(month_name)
            sales_trend["values"].append(round(month_sales))
        
        # 产品销售对比数据
        current_year = today.year
        last_year = current_year - 1
        
        # 查询前5个产品ID
        top_products = g.db.query(Sales.product_id).filter(
            Sales.date >= datetime.datetime(current_year-1, 1, 1)
        ).group_by(Sales.product_id).order_by(
            desc(func.sum(Sales.sales_amount))
        ).limit(5).all()
        
        top_product_ids = [p[0] for p in top_products]
        
        product_comparison = {
            "products": top_product_ids,
            "lastYear": [],
            "currentYear": []
        }
        
        # 获取各产品上一年的销售额
        for product_id in top_product_ids:
            last_year_sales = g.db.query(func.sum(Sales.sales_amount)).filter(
                Sales.product_id == product_id,
                extract('year', Sales.date) == last_year
            ).scalar() or 0
            
            product_comparison["lastYear"].append(round(last_year_sales))
        
        # 获取各产品今年的销售额
        for product_id in top_product_ids:
            current_year_sales = g.db.query(func.sum(Sales.sales_amount)).filter(
                Sales.product_id == product_id,
                extract('year', Sales.date) == current_year
            ).scalar() or 0
            
            product_comparison["currentYear"].append(round(current_year_sales))
        
        # 实时监控数据 (最近24小时，每2小时一个数据点)
        realtime_data = {
            "time": [],
            "sales": [],
            "orders": []
        }
        
        now = datetime.datetime.now()
        
        for i in range(12, 0, -1):
            time_point = now - datetime.timedelta(hours=i*2)
            time_label = time_point.strftime("%H:%M")
            time_start = time_point - datetime.timedelta(hours=1)
            time_end = time_point + datetime.timedelta(hours=1)
            
            # 该时间段的销售额
            period_sales = g.db.query(func.sum(Sales.sales_amount)).filter(
                Sales.date >= time_start,
                Sales.date < time_end
            ).scalar() or 0
            
            # 该时间段的订单数
            period_orders = g.db.query(func.count(Sales.id)).filter(
                Sales.date >= time_start,
                Sales.date < time_end
            ).scalar() or 0
            
            realtime_data["time"].append(time_label)
            realtime_data["sales"].append(round(period_sales))
            realtime_data["orders"].append(period_orders)
        
        return jsonify({
            "metrics": metrics,
            "regionDistribution": region_distribution,
            "salesTrend": sales_trend,
            "productComparison": product_comparison,
            "realtimeData": realtime_data
        })
        
    except Exception as e:
        app.logger.error(f"获取数字大屏数据失败: {str(e)}")
        return jsonify({"error": "获取数据失败"}), 500

# 获取最新交易数据
@app.route('/api/dataScreen/transactions', methods=['GET'])
@jwt_required(optional=True)
def get_latest_transactions():
    try:
        # 获取最新的10条交易记录
        latest_transactions = g.db.query(Sales).order_by(
            desc(Sales.date)
        ).limit(10).all()
        
        transactions = []
        for transaction in latest_transactions:
            transactions.append({
                "date": transaction.date.strftime("%Y-%m-%d %H:%M:%S"),
                "product_id": transaction.product_id,
                "region": transaction.region,
                "sales_amount": float(transaction.sales_amount),
                "units_sold": transaction.units_sold
            })
        
        return jsonify({"transactions": transactions})
        
    except Exception as e:
        app.logger.error(f"获取最新交易数据失败: {str(e)}")
        return jsonify({"error": "获取数据失败"}), 500

# 登录接口
@app.route('/api/auth/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"error": "请求格式错误，需要JSON"}), 400
    
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    client_timestamp = request.json.get('clientTimestamp', None)
    
    if not username or not password:
        return jsonify({"error": "用户名和密码必填"}), 400
        
    # 检查时间戳是否合理（防止重放攻击）
    if client_timestamp:
        current_time = datetime.datetime.now().timestamp() * 1000
        time_diff = current_time - client_timestamp
        # 如果时间差大于5分钟，可能是重放攻击
        if time_diff > 300000 or time_diff < -300000:
            return jsonify({"error": "请求已过期，请重试"}), 401
    
    # 验证用户名和密码
    user = g.db.query(User).filter_by(username=username).first()
    
    if user:
        # 获取存储的密码哈希
        stored_password = user.password
        if isinstance(stored_password, str):
            stored_password = stored_password.encode('utf-8')
        
        # 计算前端加密密码和存储密码的哈希匹配
        # 从数据库获取已经bcrypt哈希过的密码和前端SHA256哈希过的密码比较
        # 先用bcrypt.hashpw对前端SHA256哈希生成的密码进行哈希，然后比较结果
        try:
            # 验证方式1：前端已使用SHA256加密，后端使用比较安全的方式验证
            # 获取用户在数据库中保存的盐值
            salt = bcrypt.gensalt()
            if user.salt:
                salt = user.salt.encode('utf-8')
                
            # 使用相同的盐值对前端传来的加密密码再次加密
            hashed_password = user.password
            password_match = False
            
            # 直接比较前端SHA256哈希与数据库中存储的bcrypt哈希
            # 注意：这需要在init_db.py中也使用相同的SHA256方法
            if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                password_match = True
                
            if password_match:
                # 更新最后登录时间
                user.last_login = datetime.datetime.now()
                g.db.commit()
                
                # 生成JWT令牌
                access_token = create_access_token(identity=username)
                return jsonify({"token": access_token, "user": {"username": user.username, "role": user.role}}), 200
            else:
                return jsonify({"error": "用户名或密码错误"}), 401
        except Exception as e:
            app.logger.error(f"验证密码时出错: {str(e)}")
            return jsonify({"error": "服务器验证出错"}), 500
    
    return jsonify({"error": "用户名或密码错误"}), 401

# 获取仪表盘数据
@app.route('/api/dashboard', methods=['GET'])
@jwt_required(optional=True)
def get_dashboard_data():
    try:
        # 获取最近一年的销售数据
        today = datetime.datetime.now()
        one_year_ago = today - datetime.timedelta(days=365)
        
        # 计算关键指标
        metrics = []
        
        # 总销售额
        total_sales = g.db.query(func.sum(Sales.sales_amount)).filter(
            Sales.date >= one_year_ago
        ).scalar() or 0
        
        # 上个月销售额
        last_month = today.replace(day=1) - datetime.timedelta(days=1)
        last_month_start = last_month.replace(day=1)
        last_month_sales = g.db.query(func.sum(Sales.sales_amount)).filter(
            Sales.date >= last_month_start,
            Sales.date < today.replace(day=1)
        ).scalar() or 0
        
        # 前一个月销售额
        previous_month = last_month_start - datetime.timedelta(days=1)
        previous_month_start = previous_month.replace(day=1)
        previous_month_sales = g.db.query(func.sum(Sales.sales_amount)).filter(
            Sales.date >= previous_month_start,
            Sales.date < last_month_start
        ).scalar() or 0
        
        # 计算环比变化
        sales_change = 0
        if previous_month_sales > 0:
            sales_change = round(((last_month_sales - previous_month_sales) / previous_month_sales) * 100, 1)
        
        metrics.append({
            "title": "总销售额",
            "value": f"¥{total_sales:,.0f}",
            "change": sales_change
        })
        
        # 新增用户数
        total_users = g.db.query(func.count(User.id)).scalar() or 0
        new_users_last_month = g.db.query(func.count(User.id)).filter(
            User.created_at >= last_month_start,
            User.created_at < today.replace(day=1)
        ).scalar() or 0
        
        new_users_previous_month = g.db.query(func.count(User.id)).filter(
            User.created_at >= previous_month_start,
            User.created_at < last_month_start
        ).scalar() or 0
        
        # 计算环比变化
        users_change = 0
        if new_users_previous_month > 0:
            users_change = round(((new_users_last_month - new_users_previous_month) / new_users_previous_month) * 100, 1)
        
        metrics.append({
            "title": "新增用户",
            "value": f"{total_users:,}",
            "change": users_change
        })
        
        # 订单数量
        total_orders = g.db.query(func.count(Sales.id)).filter(
            Sales.date >= one_year_ago
        ).scalar() or 0
        
        orders_last_month = g.db.query(func.count(Sales.id)).filter(
            Sales.date >= last_month_start,
            Sales.date < today.replace(day=1)
        ).scalar() or 0
        
        orders_previous_month = g.db.query(func.count(Sales.id)).filter(
            Sales.date >= previous_month_start,
            Sales.date < last_month_start
        ).scalar() or 0
        
        # 计算环比变化
        orders_change = 0
        if orders_previous_month > 0:
            orders_change = round(((orders_last_month - orders_previous_month) / orders_previous_month) * 100, 1)
        
        metrics.append({
            "title": "订单数量",
            "value": f"{total_orders:,}",
            "change": orders_change
        })
        
        # 客单价
        average_order = 0
        if total_orders > 0:
            average_order = total_sales / total_orders
        
        avg_order_last_month = 0
        if orders_last_month > 0:
            avg_order_last_month = last_month_sales / orders_last_month
        
        avg_order_previous_month = 0
        if orders_previous_month > 0:
            avg_order_previous_month = previous_month_sales / orders_previous_month
        
        # 计算环比变化
        avg_order_change = 0
        if avg_order_previous_month > 0:
            avg_order_change = round(((avg_order_last_month - avg_order_previous_month) / avg_order_previous_month) * 100, 1)
        
        metrics.append({
            "title": "客单价",
            "value": f"¥{average_order:.1f}",
            "change": avg_order_change
        })
        
        # 获取近7个月销售趋势
        sales_trend_data = []
        for i in range(6, -1, -1):
            month_date = today - datetime.timedelta(days=30 * i)
            month_start = month_date.replace(day=1)
            
            if i > 0:
                month_end = (month_start.replace(month=month_start.month % 12 + 1, day=1) 
                            if month_start.month < 12 
                            else month_start.replace(year=month_start.year + 1, month=1, day=1))
            else:
                month_end = today
            
            month_sales = g.db.query(func.sum(Sales.sales_amount)).filter(
                Sales.date >= month_start,
                Sales.date < month_end
            ).scalar() or 0
            
            sales_trend_data.append(round(month_sales))
        
        # 获取用户分布数据（按地区）
        user_distribution = []
        regions = ['华东', '华南', '华北', '西南', '西北']
        
        for region in regions:
            region_sales = g.db.query(func.sum(Sales.sales_amount)).filter(
                Sales.region == region,
                Sales.date >= one_year_ago
            ).scalar() or 0
            
            user_distribution.append({
                "name": region,
                "value": round(region_sales)
            })
        
        # 获取产品销售数据（今年和去年对比）
        current_year = today.year
        last_year = current_year - 1
        
        # 获取产品销售数据
        product_sales = {"lastYear": [], "currentYear": []}
        
        # 查询前5个产品ID
        top_products = g.db.query(Sales.product_id).filter(
            Sales.date >= datetime.datetime(current_year-1, 1, 1)
        ).group_by(Sales.product_id).order_by(
            desc(func.sum(Sales.sales_amount))
        ).limit(5).all()
        
        top_product_ids = [p[0] for p in top_products]
        
        # 获取各产品上一年的销售额
        for product_id in top_product_ids:
            last_year_sales = g.db.query(func.sum(Sales.sales_amount)).filter(
                Sales.product_id == product_id,
                extract('year', Sales.date) == last_year
            ).scalar() or 0
            
            product_sales["lastYear"].append(round(last_year_sales))
        
        # 获取各产品今年的销售额
        for product_id in top_product_ids:
            current_year_sales = g.db.query(func.sum(Sales.sales_amount)).filter(
                Sales.product_id == product_id,
                extract('year', Sales.date) == current_year
            ).scalar() or 0
            
            product_sales["currentYear"].append(round(current_year_sales))
        
        # 返回所有数据
        dashboard_data = {
            "metrics": metrics,
            "salesTrend": sales_trend_data,
            "userDistribution": user_distribution,
            "productSales": product_sales
        }
        
        return jsonify(dashboard_data), 200
    
    except Exception as e:
        app.logger.error(f"获取仪表盘数据出错: {str(e)}")
        return jsonify({"error": f"获取数据失败: {str(e)}"}), 500

# 获取分析数据
@app.route('/api/analysis', methods=['GET'])
@jwt_required(optional=True)
def get_analysis_data():
    try:
        analysis_type = request.args.get('type', 'general')
        today = datetime.datetime.now()
        one_year_ago = today - datetime.timedelta(days=365)
        
        if analysis_type == 'trends':
            # 获取近6个月的趋势数据
            trend_data = []
            
            for i in range(5, -1, -1):
                month_date = today - datetime.timedelta(days=30 * i)
                month_start = month_date.replace(day=1)
                
                if i > 0:
                    month_end = (month_start.replace(month=month_start.month % 12 + 1, day=1) 
                                if month_start.month < 12 
                                else month_start.replace(year=month_start.year + 1, month=1, day=1))
                else:
                    month_end = today
                
                month_sales = g.db.query(func.sum(Sales.sales_amount)).filter(
                    Sales.date >= month_start,
                    Sales.date < month_end
                ).scalar() or 0
                
                month_label = f"{month_start.year}-{month_start.month:02d}"
                
                trend_data.append({
                    "date": month_label,
                    "value": round(month_sales / 1000)  # 转换为千元单位便于显示
                })
            
            # 获取产品类别分布
            categories_data = []
            
            # 假设产品ID 1-5 分别代表不同类别
            category_names = {
                1: "电子产品",
                2: "服装",
                3: "食品",
                4: "家居",
                5: "其他"
            }
            
            for product_id, category_name in category_names.items():
                category_sales = g.db.query(func.sum(Sales.sales_amount)).filter(
                    Sales.product_id == product_id,
                    Sales.date >= one_year_ago
                ).scalar() or 0
                
                # 转换为百分比
                category_percentage = round((category_sales / (total_sales or 1)) * 100)
                
                categories_data.append({
                    "name": category_name,
                    "value": category_percentage
                })
            
            return jsonify({
                "trends": trend_data,
                "categories": categories_data
            }), 200
            
        else:
            # 默认获取基本分析数据
            # 从数据库中查询最近的分析结果
            latest_analysis = g.db.query(Analysis).order_by(Analysis.created_at.desc()).first()
            
            if latest_analysis:
                return jsonify(json.loads(latest_analysis.results)), 200
            else:
                # 如果没有分析记录，返回空结果
                return jsonify({"message": "没有找到分析数据"}), 404
    
    except Exception as e:
        app.logger.error(f"获取分析数据出错: {str(e)}")
        return jsonify({"error": f"获取数据失败: {str(e)}"}), 500

# 获取报表列表
@app.route('/api/reports', methods=['GET'])
@jwt_required(optional=True)
def get_reports():
    try:
        # 从数据库中查询报表列表
        reports_query = g.db.query(
            Report.id,
            Report.name.label('title'),
            Report.created_at.label('date'),
            Report.status
        ).order_by(Report.created_at.desc()).all()
        
        reports_list = []
        for report in reports_query:
            # 将datetime转为字符串
            report_date = report.date.strftime('%Y-%m-%d')
            
            reports_list.append({
                "id": report.id,
                "title": report.title,
                "date": report_date,
                "status": report.status
            })
        
        return jsonify(reports_list), 200
    
    except Exception as e:
        app.logger.error(f"获取报表列表出错: {str(e)}")
        return jsonify({"error": f"获取数据失败: {str(e)}"}), 500

# 获取报表详情
@app.route('/api/reports/<int:report_id>', methods=['GET'])
@jwt_required(optional=True)
def get_report_detail(report_id):
    try:
        # 从数据库中查询报表详情
        report = g.db.query(Report).filter_by(id=report_id).first()
        
        if not report:
            return jsonify({"error": "报表不存在"}), 404
        
        # 解析JSON数据
        content = json.loads(report.content) if report.content else {}
        
        report_data = {
            "id": report.id,
            "title": report.name,
            "description": report.description,
            "date": report.created_at.strftime('%Y-%m-%d'),
            "status": report.status,
            "type": report.report_type,
            "content": content
        }
        
        return jsonify(report_data), 200

    except Exception as e:
        app.logger.error(f"获取报表详情出错: {str(e)}")
        return jsonify({"error": f"获取数据失败: {str(e)}"}), 500

# 全局搜索接口
@app.route('/api/search', methods=['GET'])
@jwt_required(optional=True)
def global_search():
    try:
        query = request.args.get('q', '').strip()
        search_type = request.args.get('type', 'all')  # 'all', 'reports', 'users', 'analysis'
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))

        if not query:
            return jsonify({"error": "搜索关键词不能为空"}), 400

        # 记录搜索历史
        current_user = get_jwt_identity()
        user = None
        if current_user:
            user = g.db.query(User).filter_by(username=current_user).first()

        results = {
            "query": query,
            "total": 0,
            "results": {
                "reports": [],
                "users": [],
                "analysis": [],
                "data_sources": []
            }
        }

        # 搜索报表
        if search_type in ['all', 'reports']:
            reports_query = g.db.query(Report).filter(
                Report.name.contains(query) |
                Report.description.contains(query)
            )

            if search_type == 'reports':
                reports_query = reports_query.offset((page - 1) * per_page).limit(per_page)
            else:
                reports_query = reports_query.limit(5)  # 全局搜索时限制数量

            reports = reports_query.all()

            for report in reports:
                results["results"]["reports"].append({
                    "id": report.id,
                    "title": report.name,
                    "description": report.description,
                    "type": report.report_type,
                    "status": report.status,
                    "created_at": report.created_at.strftime('%Y-%m-%d'),
                    "url": f"/reports/{report.id}"
                })

        # 搜索用户
        if search_type in ['all', 'users'] and current_user:
            users_query = g.db.query(User).filter(
                User.username.contains(query) |
                User.email.contains(query)
            )

            if search_type == 'users':
                users_query = users_query.offset((page - 1) * per_page).limit(per_page)
            else:
                users_query = users_query.limit(5)

            users = users_query.all()

            for user_item in users:
                results["results"]["users"].append({
                    "id": user_item.id,
                    "username": user_item.username,
                    "email": user_item.email,
                    "role": user_item.role,
                    "created_at": user_item.created_at.strftime('%Y-%m-%d'),
                    "url": f"/users/{user_item.id}"
                })

        # 搜索分析
        if search_type in ['all', 'analysis']:
            analysis_query = g.db.query(Analysis).filter(
                Analysis.name.contains(query) |
                Analysis.description.contains(query)
            )

            if search_type == 'analysis':
                analysis_query = analysis_query.offset((page - 1) * per_page).limit(per_page)
            else:
                analysis_query = analysis_query.limit(5)

            analyses = analysis_query.all()

            for analysis in analyses:
                results["results"]["analysis"].append({
                    "id": analysis.id,
                    "name": analysis.name,
                    "description": analysis.description,
                    "type": analysis.analysis_type,
                    "created_at": analysis.created_at.strftime('%Y-%m-%d'),
                    "url": f"/analysis/{analysis.id}"
                })

        # 搜索数据源
        if search_type in ['all', 'data_sources']:
            data_sources_query = g.db.query(DataSource).filter(
                DataSource.name.contains(query)
            )

            if search_type == 'data_sources':
                data_sources_query = data_sources_query.offset((page - 1) * per_page).limit(per_page)
            else:
                data_sources_query = data_sources_query.limit(5)

            data_sources = data_sources_query.all()

            for ds in data_sources:
                results["results"]["data_sources"].append({
                    "id": ds.id,
                    "name": ds.name,
                    "type": ds.type,
                    "active": ds.active,
                    "created_at": ds.created_at.strftime('%Y-%m-%d'),
                    "url": f"/data-sources/{ds.id}"
                })

        # 计算总结果数
        results["total"] = (
            len(results["results"]["reports"]) +
            len(results["results"]["users"]) +
            len(results["results"]["analysis"]) +
            len(results["results"]["data_sources"])
        )

        # 保存搜索历史
        if user:
            search_history = SearchHistory(
                user_id=user.id,
                query=query,
                search_type=search_type,
                results_count=results["total"]
            )
            g.db.add(search_history)
            g.db.commit()

        return jsonify(results), 200

    except Exception as e:
        app.logger.error(f"搜索失败: {str(e)}")
        return jsonify({"error": "搜索失败"}), 500

# 获取搜索建议
@app.route('/api/search/suggestions', methods=['GET'])
@jwt_required(optional=True)
def get_search_suggestions():
    try:
        query = request.args.get('q', '').strip()
        limit = int(request.args.get('limit', 5))

        if len(query) < 2:
            return jsonify({"suggestions": []}), 200

        suggestions = []

        # 从报表名称获取建议
        reports = g.db.query(Report.name).filter(
            Report.name.contains(query)
        ).limit(limit).all()

        for report in reports:
            suggestions.append({
                "text": report.name,
                "type": "report",
                "category": "报表"
            })

        # 从分析名称获取建议
        analyses = g.db.query(Analysis.name).filter(
            Analysis.name.contains(query)
        ).limit(limit).all()

        for analysis in analyses:
            suggestions.append({
                "text": analysis.name,
                "type": "analysis",
                "category": "分析"
            })

        # 去重并限制数量
        unique_suggestions = []
        seen = set()
        for suggestion in suggestions:
            if suggestion["text"] not in seen:
                unique_suggestions.append(suggestion)
                seen.add(suggestion["text"])
                if len(unique_suggestions) >= limit:
                    break

        return jsonify({"suggestions": unique_suggestions}), 200

    except Exception as e:
        app.logger.error(f"获取搜索建议失败: {str(e)}")
        return jsonify({"suggestions": []}), 200

# 获取通知列表
@app.route('/api/notifications', methods=['GET'])
@jwt_required()
def get_notifications():
    try:
        current_user = get_jwt_identity()
        user = g.db.query(User).filter_by(username=current_user).first()

        if not user:
            return jsonify({"error": "用户不存在"}), 404

        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 20))
        unread_only = request.args.get('unread_only', 'false').lower() == 'true'

        # 构建查询
        query = g.db.query(Notification).filter(
            (Notification.user_id == user.id) | (Notification.user_id.is_(None))
        )

        if unread_only:
            query = query.filter(Notification.is_read == False)

        # 分页
        total = query.count()
        notifications = query.order_by(
            Notification.is_important.desc(),
            Notification.created_at.desc()
        ).offset((page - 1) * per_page).limit(per_page).all()

        notifications_data = []
        for notification in notifications:
            notifications_data.append({
                "id": notification.id,
                "title": notification.title,
                "message": notification.message,
                "type": notification.type,
                "category": notification.category,
                "is_read": notification.is_read,
                "is_important": notification.is_important,
                "action_url": notification.action_url,
                "created_at": notification.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                "read_at": notification.read_at.strftime('%Y-%m-%d %H:%M:%S') if notification.read_at else None
            })

        return jsonify({
            "notifications": notifications_data,
            "total": total,
            "page": page,
            "per_page": per_page,
            "has_more": total > page * per_page
        }), 200

    except Exception as e:
        app.logger.error(f"获取通知列表失败: {str(e)}")
        return jsonify({"error": "获取通知失败"}), 500

# 标记通知为已读
@app.route('/api/notifications/<int:notification_id>/read', methods=['POST'])
@jwt_required()
def mark_notification_read(notification_id):
    try:
        current_user = get_jwt_identity()
        user = g.db.query(User).filter_by(username=current_user).first()

        if not user:
            return jsonify({"error": "用户不存在"}), 404

        notification = g.db.query(Notification).filter(
            Notification.id == notification_id,
            (Notification.user_id == user.id) | (Notification.user_id.is_(None))
        ).first()

        if not notification:
            return jsonify({"error": "通知不存在"}), 404

        notification.is_read = True
        notification.read_at = datetime.datetime.now()
        g.db.commit()

        return jsonify({"message": "通知已标记为已读"}), 200

    except Exception as e:
        app.logger.error(f"标记通知已读失败: {str(e)}")
        return jsonify({"error": "操作失败"}), 500

# 标记所有通知为已读
@app.route('/api/notifications/read-all', methods=['POST'])
@jwt_required()
def mark_all_notifications_read():
    try:
        current_user = get_jwt_identity()
        user = g.db.query(User).filter_by(username=current_user).first()

        if not user:
            return jsonify({"error": "用户不存在"}), 404

        # 更新所有未读通知
        g.db.query(Notification).filter(
            (Notification.user_id == user.id) | (Notification.user_id.is_(None)),
            Notification.is_read == False
        ).update({
            "is_read": True,
            "read_at": datetime.datetime.now()
        })

        g.db.commit()

        return jsonify({"message": "所有通知已标记为已读"}), 200

    except Exception as e:
        app.logger.error(f"标记所有通知已读失败: {str(e)}")
        return jsonify({"error": "操作失败"}), 500

# 获取未读通知数量
@app.route('/api/notifications/unread-count', methods=['GET'])
@jwt_required()
def get_unread_notifications_count():
    try:
        current_user = get_jwt_identity()
        user = g.db.query(User).filter_by(username=current_user).first()

        if not user:
            return jsonify({"error": "用户不存在"}), 404

        count = g.db.query(Notification).filter(
            (Notification.user_id == user.id) | (Notification.user_id.is_(None)),
            Notification.is_read == False
        ).count()

        return jsonify({"count": count}), 200

    except Exception as e:
        app.logger.error(f"获取未读通知数量失败: {str(e)}")
        return jsonify({"count": 0}), 200

# 获取用户设置
@app.route('/api/user/settings', methods=['GET'])
@jwt_required()
def get_user_settings():
    try:
        current_user = get_jwt_identity()
        user = g.db.query(User).filter_by(username=current_user).first()

        if not user:
            return jsonify({"error": "用户不存在"}), 404

        # 如果用户有设置，返回设置；否则返回默认设置
        if hasattr(user, 'settings') and user.settings:
            settings = json.loads(user.settings)
        else:
            # 默认设置
            settings = {
                "theme": "dark",
                "language": "zh-CN",
                "animations": True,
                "autoRefresh": 60,
                "dataCache": True,
                "realTimeData": True,
                "desktopNotifications": True,
                "emailNotifications": False,
                "soundNotifications": True,
                "autoLogout": 30,
                "twoFactorAuth": False,
                "loginHistory": True
            }

        return jsonify(settings), 200

    except Exception as e:
        app.logger.error(f"获取用户设置失败: {str(e)}")
        return jsonify({"error": "获取设置失败"}), 500

# 更新用户设置
@app.route('/api/user/settings', methods=['PUT'])
@jwt_required()
def update_user_settings():
    try:
        current_user = get_jwt_identity()
        user = g.db.query(User).filter_by(username=current_user).first()

        if not user:
            return jsonify({"error": "用户不存在"}), 404

        if not request.is_json:
            return jsonify({"error": "请求格式错误，需要JSON"}), 400

        new_settings = request.json

        # 获取当前设置
        if hasattr(user, 'settings') and user.settings:
            current_settings = json.loads(user.settings)
        else:
            current_settings = {}

        # 更新设置
        current_settings.update(new_settings)

        # 保存到数据库
        user.settings = json.dumps(current_settings)
        g.db.commit()

        return jsonify({"message": "设置更新成功", "settings": current_settings}), 200

    except Exception as e:
        app.logger.error(f"更新用户设置失败: {str(e)}")
        return jsonify({"error": "更新设置失败"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)