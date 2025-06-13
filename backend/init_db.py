from models import Base, User, DataSource, Dataset, Analysis, Report, Sales, Notification, SearchHistory
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import datetime
import random
import json
import bcrypt
from faker import Faker
import hashlib

# 加载环境变量
load_dotenv()

# 数据库连接信息
DB_URI = f"mysql+pymysql://{os.environ.get('DB_USER', 'root')}:{os.environ.get('DB_PASSWORD', 'password')}@{os.environ.get('DB_HOST', 'localhost')}:{os.environ.get('DB_PORT', '3306')}/{os.environ.get('DB_NAME', 'data_analysis')}"

# 创建数据库引擎
engine = create_engine(DB_URI)

# 密码加密函数 - 前端使用SHA256，后端使用bcrypt
def hash_password(password):
    # 先使用SHA256哈希模拟前端处理
    sha256_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    # 然后使用bcrypt存储到数据库
    return bcrypt.hashpw(sha256_hash.encode('utf-8'), bcrypt.gensalt())

# 创建表
def create_tables():
    Base.metadata.drop_all(engine)  # 先删除所有表（谨慎使用！）
    Base.metadata.create_all(engine)  # 创建所有表
    print("数据库表已创建")

# 创建示例用户数据
def create_sample_users(session):
    # 生成盐值
    admin_salt = bcrypt.gensalt()
    user_salt = bcrypt.gensalt()
    
    # 创建管理员用户 - 使用与前端一致的加密方式
    admin_pwd_hash = hashlib.sha256('admin123'.encode('utf-8')).hexdigest()
    admin_pwd = bcrypt.hashpw(admin_pwd_hash.encode('utf-8'), admin_salt)
    
    admin = User(
        username='admin',
        password=admin_pwd.decode('utf-8'),
        salt=admin_salt.decode('utf-8'),
        email='admin@example.com',
        role='admin',
        created_at=datetime.datetime.now(),
        last_login=datetime.datetime.now()
    )
    
    # 创建普通用户 - 使用与前端一致的加密方式
    user_pwd_hash = hashlib.sha256('user123'.encode('utf-8')).hexdigest()
    user_pwd = bcrypt.hashpw(user_pwd_hash.encode('utf-8'), user_salt)
    
    user = User(
        username='user',
        password=user_pwd.decode('utf-8'),
        salt=user_salt.decode('utf-8'),
        email='user@example.com',
        role='user',
        created_at=datetime.datetime.now(),
        last_login=datetime.datetime.now()
    )
    
    session.add_all([admin, user])
    session.commit()
    print("示例用户已创建")

# 创建示例数据源
def create_sample_data_sources(session):
    # 内部数据库数据源
    db_source = DataSource(
        name='内部数据库',
        type='database',
        connection_string='mysql+pymysql://user:password@localhost/sales_data',
        active=True,
        created_at=datetime.datetime.now()
    )
    
    # API数据源
    api_source = DataSource(
        name='市场API',
        type='api',
        api_key='sample_api_key_12345',
        active=True,
        created_at=datetime.datetime.now()
    )
    
    # 文件数据源
    file_source = DataSource(
        name='CSV文件',
        type='file',
        file_path='/data/user_data.csv',
        active=True,
        created_at=datetime.datetime.now()
    )
    
    session.add_all([db_source, api_source, file_source])
    session.commit()
    print("示例数据源已创建")
    return db_source, api_source, file_source

# 创建示例数据集
def create_sample_datasets(session, data_sources):
    db_source, api_source, file_source = data_sources
    
    # 销售数据集
    sales_dataset = Dataset(
        name='销售数据',
        description='包含历史销售数据，包括销售额、产品和区域信息',
        data_source_id=db_source.id,
        query='SELECT * FROM sales WHERE date >= "2023-01-01"',
        columns=json.dumps(['id', 'date', 'product_id', 'region', 'sales_amount', 'units_sold']),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    
    # 用户数据集
    users_dataset = Dataset(
        name='用户数据',
        description='包含用户注册和活跃信息',
        data_source_id=file_source.id,
        columns=json.dumps(['user_id', 'register_date', 'last_active_date', 'region', 'device']),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    
    # 产品数据集
    products_dataset = Dataset(
        name='产品数据',
        description='包含产品信息和销售数据',
        data_source_id=api_source.id,
        columns=json.dumps(['product_id', 'name', 'category', 'price', 'total_sales']),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    
    session.add_all([sales_dataset, users_dataset, products_dataset])
    session.commit()
    print("示例数据集已创建")
    return sales_dataset, users_dataset, products_dataset

# 创建示例分析
def create_sample_analyses(session, datasets):
    sales_dataset, users_dataset, products_dataset = datasets
    
    # 销售趋势分析
    sales_trend_analysis = Analysis(
        name='销售趋势分析',
        description='分析月度和季度销售趋势',
        dataset_id=sales_dataset.id,
        analysis_type='time_series',
        parameters=json.dumps({
            'time_column': 'date',
            'value_column': 'sales_amount',
            'group_by': 'month'
        }),
        results=json.dumps({
            'metrics': [
                { 'title': '总销售额', 'value': '¥120,000', 'change': 12.5 },
                { 'title': '新增用户', 'value': '1,520', 'change': 3.8 },
                { 'title': '订单数量', 'value': '2,450', 'change': -2.3 },
                { 'title': '客单价', 'value': '¥48.9', 'change': 8.2 }
            ],
            'salesTrend': [30000, 28000, 36000, 42000, 45000, 50000, 60000],
            'userDistribution': [
                { 'name': '华东', 'value': 1048 },
                { 'name': '华南', 'value': 735 },
                { 'name': '华北', 'value': 580 },
                { 'name': '西南', 'value': 484 },
                { 'name': '西北', 'value': 300 }
            ],
            'productSales': {
                'lastYear': [320, 302, 301, 334, 390],
                'currentYear': [420, 382, 391, 434, 490]
            }
        }),
        created_at=datetime.datetime.now()
    )
    
    # 用户增长分析
    user_growth_analysis = Analysis(
        name='用户增长分析',
        description='分析用户增长率和活跃度',
        dataset_id=users_dataset.id,
        analysis_type='trend',
        parameters=json.dumps({
            'time_column': 'register_date',
            'group_by': 'month'
        }),
        results=json.dumps({
            'labels': ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
            'datasets': [
                {
                    'label': '新增用户',
                    'data': [120, 132, 145, 162, 178, 195, 210, 225, 242, 258, 275, 290],
                    'borderColor': '#4CAF50',
                    'backgroundColor': 'rgba(76, 175, 80, 0.1)'
                },
                {
                    'label': '活跃用户',
                    'data': [450, 480, 512, 535, 560, 590, 615, 640, 660, 685, 710, 740],
                    'borderColor': '#FF9800',
                    'backgroundColor': 'rgba(255, 152, 0, 0.1)'
                }
            ],
            'summary': {
                'totalNewUsers': 2432,
                'averageNewUsers': 202.67,
                'totalActiveUsers': 7177,
                'averageActiveUsers': 598.08
            }
        }),
        created_at=datetime.datetime.now()
    )
    
    # 产品销售分析
    product_analysis = Analysis(
        name='产品销售分析',
        description='分析各产品销售情况及对比',
        dataset_id=products_dataset.id,
        analysis_type='comparison',
        parameters=json.dumps({
            'group_by': 'product_id',
            'compare_with_previous': True
        }),
        results=json.dumps({
            'labels': ['产品A', '产品B', '产品C', '产品D', '产品E', '产品F'],
            'datasets': [
                {
                    'label': '2023年销量',
                    'data': [1245, 980, 1350, 850, 720, 450],
                    'borderColor': '#673AB7',
                    'backgroundColor': 'rgba(103, 58, 183, 0.1)'
                },
                {
                    'label': '2022年销量',
                    'data': [1050, 920, 1090, 780, 680, 420],
                    'borderColor': '#9E9E9E',
                    'backgroundColor': 'rgba(158, 158, 158, 0.1)'
                }
            ],
            'summary': {
                'total': 5595,
                'average': 932.5,
                'max': 1350,
                'min': 450
            }
        }),
        created_at=datetime.datetime.now()
    )
    
    session.add_all([sales_trend_analysis, user_growth_analysis, product_analysis])
    session.commit()
    print("示例分析已创建")
    return sales_trend_analysis, user_growth_analysis, product_analysis

# 创建示例报表
def create_sample_reports(session, analyses, users):
    admin = users[0]
    sales_trend_analysis, user_growth_analysis, product_analysis = analyses
    
    # 月度销售报表
    sales_report = Report(
        name='2023年第一季度销售报告',
        description='第一季度销售情况总结及趋势分析',
        user_id=admin.id,
        analysis_id=sales_trend_analysis.id,
        report_type='sales',
        status='completed',
        content=json.dumps({
            'summary': '第一季度销售额达到94,000元，同比增长12.5%。',
            'charts': [
                {'type': 'line', 'data': {'labels': ['1月', '2月', '3月'], 'datasets': [{'label': '销售额', 'data': [30000, 28000, 36000]}]}}
            ]
        }),
        created_at=datetime.datetime(2023, 4, 1),
        updated_at=datetime.datetime(2023, 4, 1)
    )
    
    # 用户增长分析报表
    user_report = Report(
        name='用户增长分析',
        description='用户增长趋势及活跃度分析',
        user_id=admin.id,
        analysis_id=user_growth_analysis.id,
        report_type='users',
        status='completed',
        content=json.dumps({
            'summary': '用户增长率保持在5%左右，但活跃度有所下降。',
            'charts': [
                {'type': 'line', 'data': {'labels': ['1月', '2月', '3月', '4月'], 'datasets': [{'label': '新增用户', 'data': [120, 132, 145, 162]}]}}
            ]
        }),
        created_at=datetime.datetime(2023, 4, 15),
        updated_at=datetime.datetime(2023, 4, 15)
    )
    
    # 产品销售对比报表
    product_report = Report(
        name='产品性能评估',
        description='各产品销售情况对比及性能评估',
        user_id=admin.id,
        analysis_id=product_analysis.id,
        report_type='products',
        status='processing',
        content=json.dumps({
            'summary': '产品C表现最佳，建议增加库存。',
            'charts': [
                {'type': 'bar', 'data': {'labels': ['产品A', '产品B', '产品C'], 'datasets': [{'label': '销量', 'data': [1245, 980, 1350]}]}}
            ]
        }),
        created_at=datetime.datetime(2023, 5, 1),
        updated_at=datetime.datetime(2023, 5, 1)
    )
    
    session.add_all([sales_report, user_report, product_report])
    session.commit()
    print("示例报表已创建")

# 生成更多的销售数据
def generate_sales_data(session):
    fake = Faker()
    
    # 重新创建销售表
    Sales.__table__.drop(engine, checkfirst=True)
    Sales.__table__.create(engine)
    
    # 地区列表
    regions = ['华东', '华南', '华北', '西南', '西北']
    
    # 产品列表
    products = list(range(1, 6))  # 5个产品
    
    # 生成销售数据
    sales_records = []
    
    # 第一部分：生成历史销售数据（2022年1月至2023年）
    start_date = datetime.datetime(2022, 1, 1)
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    current_day = datetime.datetime.now().day
    previous_month_end = datetime.datetime(current_year, current_month, 1) - datetime.timedelta(days=1)
    
    # 生成2022年至上个月末的销售数据
    current_date = start_date
    while current_date <= previous_month_end:
        # 每天5-15条销售记录
        daily_records = random.randint(5, 15)
        
        for _ in range(daily_records):
            product_id = random.choice(products)
            region = random.choice(regions)
            units = random.randint(1, 10)
            price = random.uniform(50, 200)
            amount = units * price
            
            # 模拟一些季节性变化
            month = current_date.month
            if month in [11, 12, 1]:  # 冬季促销
                amount *= random.uniform(1.2, 1.5)
            elif month in [6, 7, 8]:  # 夏季促销
                amount *= random.uniform(1.1, 1.3)
            
            # 添加年度增长因素
            year_factor = 1.0 + (current_date.year - 2022) * 0.15  # 每年增长15%
            amount *= year_factor
            
            sale_time = current_date.replace(
                hour=random.randint(9, 18),
                minute=random.randint(0, 59),
                second=random.randint(0, 59)
            )
            
            sales_record = Sales(
                date=sale_time,
                product_id=product_id,
                region=region,
                sales_amount=round(amount, 2),
                units_sold=units
            )
            sales_records.append(sales_record)
        
        current_date += datetime.timedelta(days=1)
    
    # 第二部分：生成当月详细数据（每小时更多的数据点）
    current_month_start = datetime.datetime(current_year, current_month, 1)
    today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    
    # 生成当月至今的数据（更密集）
    current_date = current_month_start
    while current_date <= today:
        # 每天15-30条销售记录
        daily_records = random.randint(15, 30)
        
        for _ in range(daily_records):
            product_id = random.choice(products)
            region = random.choice(regions)
            units = random.randint(1, 15)
            price = random.uniform(60, 220)  # 略微提高价格
            amount = units * price
            
            # 添加促销因素
            if current_date.weekday() >= 5:  # 周末
                amount *= random.uniform(1.1, 1.25)  # 周末销售额增加
            
            sale_time = current_date.replace(
                hour=random.randint(8, 22),  # 更长的营业时间
                minute=random.randint(0, 59),
                second=random.randint(0, 59)
            )
            
            sales_record = Sales(
                date=sale_time,
                product_id=product_id,
                region=region,
                sales_amount=round(amount, 2),
                units_sold=units
            )
            sales_records.append(sales_record)
        
        current_date += datetime.timedelta(days=1)
    
    # 第三部分：生成今天的实时数据（每小时多条记录）
    now = datetime.datetime.now()
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    
    # 生成今天每小时的数据
    for hour in range(0, now.hour + 1):
        # 每小时5-20条记录
        hourly_records = random.randint(5, 20)
        
        for _ in range(hourly_records):
            product_id = random.choice(products)
            region = random.choice(regions)
            units = random.randint(1, 8)
            price = random.uniform(70, 250)  # 今日特价
            amount = units * price
            
            # 模拟早晚高峰
            if hour in [9, 10, 11, 18, 19, 20]:
                amount *= random.uniform(1.2, 1.4)  # 高峰期销售增加
            
            sale_time = today_start.replace(
                hour=hour,
                minute=random.randint(0, 59),
                second=random.randint(0, 59)
            )
            
            sales_record = Sales(
                date=sale_time,
                product_id=product_id,
                region=region,
                sales_amount=round(amount, 2),
                units_sold=units
            )
            sales_records.append(sales_record)
    
    # 批量添加销售记录
    session.add_all(sales_records)
    session.commit()
    print(f"已生成 {len(sales_records)} 条销售数据记录")

# 主函数
def main():
    # 创建会话工厂
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        # 创建表
        create_tables()
        
        # 创建示例数据
        create_sample_users(session)
        data_sources = create_sample_data_sources(session)
        datasets = create_sample_datasets(session, data_sources)
        analyses = create_sample_analyses(session, datasets)
        users = session.query(User).all()
        create_sample_reports(session, analyses, users)
        
        # 生成销售数据
        generate_sales_data(session)
        
        print("数据库初始化完成！")
    
    except Exception as e:
        print(f"初始化数据库时出错: {e}")
        session.rollback()
    
    finally:
        session.close()

if __name__ == "__main__":
    main() 