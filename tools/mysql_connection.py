from sqlalchemy import create_engine
from sqlalchemy.orm import Session
# from main import data_dict


# class MysqlConnection:
#     def __init__(self):
        # mysql_settings = data_dict['mysql_settings']
        # print('>> 连接MySQL...')
        # self.engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8mb4'
        #                             % (mysql_settings['MYSQL_USER'],
        #                                mysql_settings['MYSQL_PASSWORD'],
        #                                mysql_settings['MYSQL_HOST'],
        #                                mysql_settings['MYSQL_PORT'],
        #                                mysql_settings['MYSQL_DB']))
        # print('>> 已连接数据表。')
        # # 建立链接游标
        # self.session = Session(self.engine.connect())
        # self.cursor = self.session.connection().connection.cursor()
        # self.cursor.fast_executemany = True
