#!/usr/bin/env python3
"""
创建示例通知数据的脚本
"""

import os
import sys
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models import User, Notification, SearchHistory

# 加载环境变量
load_dotenv()

# 数据库连接
DB_URI = f"mysql+pymysql://{os.environ.get('DB_USER', 'root')}:{os.environ.get('DB_PASSWORD', 'password')}@{os.environ.get('DB_HOST', 'localhost')}:{os.environ.get('DB_PORT', '3306')}/{os.environ.get('DB_NAME', 'data_analysis')}"

def create_sample_notifications():
    """创建示例通知数据"""
    
    engine = create_engine(DB_URI)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        # 获取第一个用户
        user = session.query(User).first()
        if not user:
            print("没有找到用户，请先创建用户")
            return
        
        # 清除现有通知
        session.query(Notification).delete()
        session.commit()
        
        # 创建示例通知
        notifications = [
            {
                'user_id': user.id,
                'title': '欢迎使用数据分析平台',
                'message': '欢迎您使用我们的数据分析平台！您可以在这里查看各种数据报表和分析结果。',
                'type': 'info',
                'category': 'system',
                'is_read': False,
                'is_important': True,
                'action_url': '/dashboard',
                'created_at': datetime.datetime.now() - datetime.timedelta(hours=1)
            },
            {
                'user_id': user.id,
                'title': '新报表生成完成',
                'message': '您的月度销售报表已经生成完成，请查看最新的销售数据分析。',
                'type': 'success',
                'category': 'report',
                'is_read': False,
                'is_important': False,
                'action_url': '/reports',
                'created_at': datetime.datetime.now() - datetime.timedelta(minutes=30)
            },
            {
                'user_id': user.id,
                'title': '数据同步警告',
                'message': '检测到部分数据源同步异常，可能影响报表准确性，请及时处理。',
                'type': 'warning',
                'category': 'system',
                'is_read': False,
                'is_important': True,
                'action_url': '/data-sources',
                'created_at': datetime.datetime.now() - datetime.timedelta(minutes=15)
            },
            {
                'user_id': user.id,
                'title': '分析任务完成',
                'message': '您的销售趋势分析任务已完成，发现了一些有趣的数据模式。',
                'type': 'success',
                'category': 'analysis',
                'is_read': True,
                'is_important': False,
                'action_url': '/analysis',
                'created_at': datetime.datetime.now() - datetime.timedelta(hours=2),
                'read_at': datetime.datetime.now() - datetime.timedelta(hours=1)
            },
            {
                'user_id': None,  # 系统通知
                'title': '系统维护通知',
                'message': '系统将于今晚23:00-01:00进行例行维护，期间可能影响部分功能使用。',
                'type': 'info',
                'category': 'system',
                'is_read': False,
                'is_important': True,
                'action_url': None,
                'created_at': datetime.datetime.now() - datetime.timedelta(minutes=45)
            },
            {
                'user_id': user.id,
                'title': '存储空间不足',
                'message': '您的数据存储空间使用率已达到85%，建议清理旧数据或升级存储方案。',
                'type': 'warning',
                'category': 'system',
                'is_read': False,
                'is_important': False,
                'action_url': '/settings',
                'created_at': datetime.datetime.now() - datetime.timedelta(hours=3)
            },
            {
                'user_id': user.id,
                'title': '新功能上线',
                'message': '我们新增了智能数据预测功能，快来体验AI驱动的数据分析吧！',
                'type': 'info',
                'category': 'system',
                'is_read': True,
                'is_important': False,
                'action_url': '/analysis',
                'created_at': datetime.datetime.now() - datetime.timedelta(days=1),
                'read_at': datetime.datetime.now() - datetime.timedelta(hours=12)
            },
            {
                'user_id': user.id,
                'title': '报表导出失败',
                'message': '您请求的Excel报表导出失败，请检查数据格式或重试。',
                'type': 'error',
                'category': 'report',
                'is_read': False,
                'is_important': False,
                'action_url': '/reports',
                'created_at': datetime.datetime.now() - datetime.timedelta(minutes=10)
            }
        ]
        
        # 添加通知到数据库
        for notification_data in notifications:
            notification = Notification(**notification_data)
            session.add(notification)
        
        # 创建一些搜索历史记录
        search_histories = [
            {
                'user_id': user.id,
                'query': '销售报表',
                'search_type': 'global',
                'results_count': 5,
                'created_at': datetime.datetime.now() - datetime.timedelta(hours=2)
            },
            {
                'user_id': user.id,
                'query': '用户分析',
                'search_type': 'analysis',
                'results_count': 3,
                'created_at': datetime.datetime.now() - datetime.timedelta(hours=4)
            },
            {
                'user_id': user.id,
                'query': '数据源',
                'search_type': 'global',
                'results_count': 2,
                'created_at': datetime.datetime.now() - datetime.timedelta(days=1)
            }
        ]
        
        for history_data in search_histories:
            history = SearchHistory(**history_data)
            session.add(history)
        
        session.commit()
        print(f"成功创建了 {len(notifications)} 条通知和 {len(search_histories)} 条搜索历史")
        
    except Exception as e:
        print(f"创建示例数据失败: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == '__main__':
    create_sample_notifications()
