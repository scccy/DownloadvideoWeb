import aiohttp
import asyncio
import os
import json


from sqlalchemy import create_engine
from sqlalchemy.orm import Session

MYSQL_HOST = '192.168.31.85'
MYSQL_PORT = '5306'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'asdsc88Q12'
MYSQL_DB = 'dy_gather'


# 拼接下载数据
def search_date():
    print('>> 连接MySQL...')
    engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8mb4'
                           % (MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DB))
    print('>> 已连接数据表。')
    # 建立链接游标
    session = Session(engine.connect())
    cursor = session.connection().connection.cursor()
    cursor.fast_executemany = True
    search_sql = "select * from dy_gather.gather_day where 是否上传 = 1"
    row = cursor.execute(search_sql)
    header = [i[0] for i in cursor.description]
    while row == 0:
        print("没有数据")
    while row == 1:
        result = cursor.fetchone()
        dictionary = dict(zip(header, result))
        return dictionary
    else:
        result = cursor.fetchall()
        dictionary_list = list()
        for date in result:
            dictionary = dict(zip(header, date))
            dictionary_list.append(dictionary)
        return dictionary_list
    cursor.close()
    session.close()
    engine.dispose()


# 处理json 获取url
def get_url():
    date = search_date()
    date_list = list()
    if type(date) is dict:
        date_list.append(dispose_date(date))
        return date_list
    if type(date) is list:
        for i in range(len(date)):
            date_list.append(dispose_date(date[i]))
        return date_list


def dispose_date(date):
    post_json = {}
    post_json = json.loads(json.dumps(post_json))
    post_json['uid'] = date['UID']
    post_json['uuid'] = date['作品ID']
    post_json['账号昵称'] = date['账号昵称']
    post_json['tag'] = date['作品描述']
    post_json['view_url'] = date['下载地址']
    post_json['cover'] = date['静态封面']
    post_json['save_path'] = "V:\\test\\TikTokDownloader-master\\Download\\" + date['账号昵称'] + "\\"
    return post_json


async def download_file(url, save_path, file_name):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            print(file_name)
            with open(save_path + file_name, 'wb') as f:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)
    return save_path + file_name


async def main(url_jsonlist):
    tasks = [
        download_file(file['view_url'], file['save_path'], file['uuid'] + '.mp4') for file in url_jsonlist
    ]

    downloaded_files = await asyncio.gather(*tasks)
    for downloaded_file in downloaded_files:
        print(f'File downloaded to: {downloaded_file}')


if __name__ == '__main__':
    try:
        print(os.path.join(os.getcwd(), 'downloaded_file1.mp4'))
        result_url = get_url()
        asyncio.run(main(result_url))

    except Exception as e:
        print(e)
#
