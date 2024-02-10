import requests
import json
import pandas as pd
from DownloadvideoWeb import settings
from DownloadvideoWeb.settings import server_url


def search_data(json_data):
    url = server_url
    payload = json.dumps({
        "keyword": json_data['keyword'],
        "type": json_data['type'],
        "pages": json_data['pages'],
        "sort_type": json_data['sort_type'],
        "publish_time": json_data['publish_time'],
        "source": False
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_data = response.json()
    return response_data


def save_search_data(search):
    update_list = list()
    if search['message'] == 'success':
        for i in range(len(search['data'])):
            update_dict = dict()
            data = search['data'][i]
            update_dict['作品类型'] = data['type']
            update_dict['采集时间'] = data['collection_time']
            update_dict['UID'] = data['uid']
            update_dict['SEC_UID'] = data['sec_uid']
            update_dict['抖音号'] = data['unique_id']
            update_dict['SHORT_ID'] = data['id']
            update_dict['作品描述'] = data['desc']
            update_dict['作品话题'] = data['type']
            update_dict['视频时长'] = data['duration']
            update_dict['视频分辨率'] = data['ratio']
            update_dict['视频高度'] = data['height']
            update_dict['视频宽度'] = data['width']
            update_dict['作品链接'] = data['share_url']
            update_dict['发布时间'] = data['create_time']
            update_dict['视频URI'] = data['v0200fg10000cn2qec3c77u4kffvf06g']
            update_dict['账号昵称'] = data['nickname']
            update_dict['年龄'] = data['user_age']
            update_dict['账号签名'] = data['signature']
            update_dict['下载地址'] = data['downloads']
            update_dict['音乐作者'] = data['music_author']
            update_dict['音乐标题'] = data['music_title']
            update_dict['音乐链接'] = data['music_url']
            update_dict['静态封面'] = data['origin_cover']
            update_dict['动态封面'] = data['dynamic_cover']
            update_dict['标签_1'] = data['tag_1']
            update_dict['标签_2'] = data['tag_2']
            update_dict['标签_3'] = data['tag_3']
            update_dict['点赞数量'] = data['digg_count']
            update_dict['评论数量'] = data['comment_count']
            update_dict['收藏数量'] = data['collect_count']
            update_dict['分享数量'] = data['share_count']
            update_dict['额外信息'] = data['extra']
            update_dict['是否上传'] = 0
            update_dict['上传成功'] = 0
            update_dict['是否删除文件'] = 0
            update_list.append(update_dict)
