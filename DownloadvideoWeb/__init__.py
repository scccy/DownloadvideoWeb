import pymysql
from sqlalchemy import create_engine
from DownloadvideoWeb import settings
from sqlalchemy.orm import sessionmaker, scoped_session, DeclarativeBase

pymysql.install_as_MySQLdb()


class Base(DeclarativeBase):
    pass


engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8mb4'
                       % (settings.MYSQL_USER, settings.MYSQL_PASSWORD, settings.MYSQL_HOST,
                          settings.MYSQL_PORT, settings.MYSQL_DBNAME))
create_engine('sqlite:///:memory:', echo=True)

# 创建 Session 类
Session = sessionmaker(bind=engine)
session = scoped_session(Session)
# 注册 User 类到映射中
Base.metadata.create_all(engine)
