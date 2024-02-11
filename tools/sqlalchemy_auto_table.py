from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from DownloadvideoWeb import settings
#
#
# # 替换为你的数据库连接信息
# engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8mb4'
#                        % (settings.MYSQL_USER, settings.MYSQL_PASSWORD, settings.MYSQL_HOST,
#                           settings.MYSQL_PORT, settings.MYSQL_DBNAME))
# print('mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8mb4'
#                        % (settings.MYSQL_USER, settings.MYSQL_PASSWORD, settings.MYSQL_HOST,
#                           settings.MYSQL_PORT, settings.MYSQL_DBNAME))
# engine.dispose()
# metadata = MetaData()
#
# # 反射数据库表结构
# metadata.reflect(engine)
#
# # 使用automap_base创建一个Base类，它会自动为所有表创建一个映射
# Base = automap_base(metadata=metadata)
# Base.prepare()
# # 也可以这样：Base.prepare(engine, reflect=True)
#
# # 将映射的表名与类关联
# YourTable = Base.classes.gather_day
#
# # 创建会话
# Session = sessionmaker(bind=engine)
# session = Session()
#
# # 从模型中查询数据
# results = session.query(YourTable).all()
#
# # 打印查询结果
# for result in results:
#     print(result)
