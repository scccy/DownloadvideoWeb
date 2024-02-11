from sqlalchemy import create_engine
from DownloadvideoWeb import settings


engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8mb4'
                       % (settings.MYSQL_USER, settings.MYSQL_PASSWORD, settings.MYSQL_HOST,
                          settings.MYSQL_PORT, settings.MYSQL_DBNAME))

