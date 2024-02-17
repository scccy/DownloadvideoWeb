from datetime import datetime
from django.db import models
from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME, TEXT
from sqlalchemy.orm import relationship, Mapped, mapped_column

from DownloadvideoWeb import session, Base, engine


# 关键词搜索模型

class GatherDay(Base):
    __tablename__ = "gather_day"
    type = Column(String(255))
    collection_time = Column(DATETIME)
    uid = Column(String(255), primary_key=True)
    video_id = Column(String(255), primary_key=True)
    sec_uid = Column(String(255))
    unique_id = Column(String(255))
    short_id = Column(String(255))
    desc = Column(String(255))
    text_extra = Column(String(255))
    duration = Column(String(255))
    ratio = Column(String(255))
    height = Column(Integer)
    width = Column(Integer)
    share_url = Column(TEXT)
    create_time = Column(DATETIME)
    uri = Column(String(255))
    nickname = Column(String(255))
    user_age = Column(String(255))
    signature = Column(String(255))
    downloads = Column(TEXT)
    music_author = Column(String(255))
    music_title = Column(String(255))
    music_url = Column(TEXT)
    origin_cover = Column(TEXT)
    dynamic_cover = Column(TEXT)
    tag_1 = Column(String(255))
    tag_2 = Column(String(255))
    tag_3 = Column(String(255))
    digg_count = Column(Integer)
    comment_count = Column(Integer)
    collect_count = Column(Integer)
    share_count = Column(Integer)
    extra = Column(TEXT)
    load_if = Column(Integer)
    load_sts = Column(Integer)
    del_if = Column(Integer)


def __init__(self, **kwargs):
    for key, value in kwargs.items():
        if hasattr(self, key):
            setattr(self, key, value)


# 注册 User 类到映射中
Base.metadata.create_all(engine)
