# -- coding: utf-8 --

import pandas as pd
import glob
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

current_dateTime = datetime.now().strftime('%Y_%m_%d')

MYSQL_HOST = '192.168.31.85'
MYSQL_PORT = '5306'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'asdsc88Q12'
MYSQL_DB = 'dy_gather'


class GatherCsv:
    def __init__(self):
        print('>> 连接MySQL...')
        self.engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8mb4'
                                    % (MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DB))
        print('>> 已连接数据表。')
        # 建立链接游标
        self.session = Session(self.engine.connect())
        self.cursor = self.session.connection().connection.cursor()
        self.cursor.fast_executemany = True

    # 查找今日采集文件
    def search_file(self):
        file_out_dir = "Data/搜索数据" + "_{0}".format(current_dateTime) + "*.csv"
        file_list = glob.glob(file_out_dir)
        for file in file_list:
            self.read_file(file)

    # 上传csv到MySQL
    def read_file(self, file):
        df = pd.read_csv(file)
        df.insert(loc=len(df.columns), column='是否上传', value=0)
        df.insert(loc=len(df.columns), column='是否删除文件', value=0)
        df.to_sql('temp', self.engine, if_exists='replace', index=False)
        replacer_sql = """
             REPLACE INTO gather_day
                     SELECT * FROM temp
            """
        self.cursor.execute(replacer_sql)
        args2 = """ DROP Table If Exists temp """  # 把临时表删除
        self.cursor.execute(args2)

        # 上传csv到MySQL

    def update_df(self, df, table_name):
        df.insert(loc=len(df.columns), column='是否上传', value=0)
        df.insert(loc=len(df.columns), column='是否删除文件', value=0)
        df.to_sql('temp', self.engine, if_exists='replace', index=False)
        replacer_sql = """
               REPLACE INTO {0}
                       SELECT * FROM temp
              """.format(table_name)
        self.cursor.execute(replacer_sql)
        args2 = """ DROP Table If Exists temp """  # 把临时表删除
        self.cursor.execute(args2)

    def main(self):
        try:
            self.search_file()
            self.cursor.commit()
            self.session.close()
            self.cursor.close()
            self.engine.dispose()
        except Exception as e:
            print(e)

