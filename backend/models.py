from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os
from dotenv import load_dotenv
import datetime

# 加载环境变量
load_dotenv()

# 数据库连接
DB_URI = f"mysql+pymysql://{os.environ.get('DB_USER', 'root')}:{os.environ.get('DB_PASSWORD', 'password')}@{os.environ.get('DB_HOST', 'localhost')}:{os.environ.get('DB_PORT', '3306')}/{os.environ.get('DB_NAME', 'data_analysis')}"
engine = create_engine(DB_URI)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)  # 存储密码哈希值
    salt = Column(String(255), nullable=True)  # 存储密码盐值
    email = Column(String(100), unique=True, nullable=False)
    role = Column(String(20), default='user')
    settings = Column(Text, nullable=True)  # 存储用户设置的JSON字符串
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    last_login = Column(DateTime, nullable=True)

    reports = relationship("Report", back_populates="user")

    def __repr__(self):
        return f"<User {self.username}>"

class DataSource(Base):
    __tablename__ = 'data_sources'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50), nullable=False)  # 'database', 'api', 'file'
    connection_string = Column(String(255), nullable=True)
    api_key = Column(String(255), nullable=True)
    file_path = Column(String(255), nullable=True)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    datasets = relationship("Dataset", back_populates="data_source")
    
    def __repr__(self):
        return f"<DataSource {self.name}>"

class Dataset(Base):
    __tablename__ = 'datasets'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    data_source_id = Column(Integer, ForeignKey('data_sources.id'))
    query = Column(Text, nullable=True)
    columns = Column(Text, nullable=True)  # 存储为JSON字符串
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    
    data_source = relationship("DataSource", back_populates="datasets")
    analyses = relationship("Analysis", back_populates="dataset")
    
    def __repr__(self):
        return f"<Dataset {self.name}>"

class Analysis(Base):
    __tablename__ = 'analyses'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    dataset_id = Column(Integer, ForeignKey('datasets.id'))
    analysis_type = Column(String(50), nullable=False)  # 'time_series', 'correlation', 'regression', etc.
    parameters = Column(Text, nullable=True)  # 存储为JSON字符串
    results = Column(Text, nullable=True)  # 存储为JSON字符串
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    dataset = relationship("Dataset", back_populates="analyses")
    reports = relationship("Report", back_populates="analysis")
    
    def __repr__(self):
        return f"<Analysis {self.name}>"

class Report(Base):
    __tablename__ = 'reports'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    analysis_id = Column(Integer, ForeignKey('analyses.id'))
    report_type = Column(String(50), nullable=False)  # 'sales', 'users', 'products', etc.
    status = Column(String(20), default='draft')  # 'draft', 'processing', 'completed'
    content = Column(Text, nullable=True)  # 存储为JSON字符串
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    
    user = relationship("User", back_populates="reports")
    analysis = relationship("Analysis", back_populates="reports")
    
    def __repr__(self):
        return f"<Report {self.name}>"

# 添加Sales类
class Sales(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    product_id = Column(Integer, nullable=False)
    region = Column(String(50), nullable=False)
    sales_amount = Column(Float, nullable=False)
    units_sold = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Sales {self.id}>"

# 通知模型
class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)  # 如果为空则为系统通知
    title = Column(String(200), nullable=False)
    message = Column(Text, nullable=False)
    type = Column(String(50), default='info')  # 'info', 'success', 'warning', 'error'
    category = Column(String(50), default='system')  # 'system', 'report', 'analysis', 'user'
    is_read = Column(Boolean, default=False)
    is_important = Column(Boolean, default=False)
    action_url = Column(String(255), nullable=True)  # 点击通知后跳转的URL
    extra_data = Column(Text, nullable=True)  # 存储额外信息的JSON字符串
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    read_at = Column(DateTime, nullable=True)

    user = relationship("User", backref="notifications")

    def __repr__(self):
        return f"<Notification {self.title}>"

# 搜索历史模型
class SearchHistory(Base):
    __tablename__ = 'search_history'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    query = Column(String(255), nullable=False)
    search_type = Column(String(50), default='global')  # 'global', 'reports', 'analysis'
    results_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", backref="search_history")

    def __repr__(self):
        return f"<SearchHistory {self.query}>"

# 创建所有表
def init_db():
    Base.metadata.create_all(engine)
