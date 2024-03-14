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
    keyword = Column(String(255))

    @staticmethod
    def to_str(GatherDay):
        return {
            'type': GatherDay.type,
            'collection_time': str(GatherDay.collection_time),
            'uid': GatherDay.uid,
            'video_id': GatherDay.video_id,
            'sec_uid': GatherDay.sec_uid,
            'unique_id': GatherDay.unique_id,
            'short_id': GatherDay.short_id,
            'desc': GatherDay.desc,
            'text_extra': GatherDay.text_extra,
            'duration': GatherDay.duration,
            'ratio': GatherDay.ratio,
            'height': GatherDay.height,
            'width': GatherDay.width,
            'share_url': GatherDay.share_url,
            'create_time': str(GatherDay.create_time),
            'uri': GatherDay.uri,
            'nickname': GatherDay.nickname,
            'user_age': GatherDay.user_age,
            'signature': GatherDay.signature,
            'downloads': GatherDay.downloads,
            'music_author': GatherDay.music_author,
            'music_title': GatherDay.music_title,
            'music_url': GatherDay.music_url,
            'origin_cover': GatherDay.origin_cover,
            'dynamic_cover': GatherDay.dynamic_cover,
            'tag_1': GatherDay.tag_1,
            'tag_2': GatherDay.tag_2,
            'tag_3': GatherDay.tag_3,
            'digg_count': GatherDay.digg_count,
            'comment_count': GatherDay.comment_count,
            'collect_count': GatherDay.collect_count,
            'share_count': GatherDay.share_count,
            'extra': GatherDay.extra,
            'load_if': GatherDay.load_if,
            'load_sts': GatherDay.load_sts,
            'del_if': GatherDay.del_if,
            'keyword': GatherDay.keyword
        }
