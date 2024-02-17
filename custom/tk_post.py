import json

import requests
from flow_tk.models import GatherDay
from DownloadvideoWeb import session
from DownloadvideoWeb.settings import server_url
from sqlalchemy import select

headers = {
    'Content-Type': 'application/json'
}


def search_data(json_data):
    url = server_url + 'search/'
    payload = json.dumps({
        "keyword": json_data['keyword'],
        "type": json_data['type'],
        "pages": json_data['pages'],
        "sort_type": json_data['sort_type'],
        "publish_time": json_data['publish_time'],
        "source": False
    })

    response = requests.request("POST", url, headers=headers, data=payload)
    response_data = response.json()
    return response_data


# 按账号下载
def search_data_by_account(json_data):
    url = server_url + 'account/'
    payload = json.dumps({
        "url": json_data['url'],
        "tab": json_data['tab'],
        "earliest": json_data['earliest'],
        "latest": json_data['latest'],
        "source": False
    })

    response = requests.request("POST", url, headers=headers, data=payload)
    response_data = response.json()
    return response_data


def search_data_save(search):
    try:
        if search['message'] == 'success':
            for i in range(len(search['data'])):
                update_dict = dict()
                data = search['data'][i]
                update_dict['video_id'] = data['id']
                update_dict['type'] = data['type']
                update_dict['collection_time'] = data['collection_time']
                update_dict['uid'] = data['uid']
                update_dict['sec_uid'] = data['sec_uid']
                update_dict['unique_id'] = data['unique_id']
                update_dict['short_id'] = data['short_id']
                update_dict['desc'] = data['desc']
                update_dict['text_extra'] = data['text_extra']
                update_dict['duration'] = data['duration']
                update_dict['ratio'] = data['ratio']
                update_dict['height'] = data['height']
                update_dict['width'] = data['width']
                update_dict['share_url'] = data['share_url']
                update_dict['create_time'] = data['create_time']
                update_dict['uri'] = data['uri']
                update_dict['nickname'] = data['nickname']
                update_dict['user_age'] = data['user_age']
                update_dict['signature'] = data['signature']
                update_dict['downloads'] = data['downloads']
                update_dict['music_author'] = data['music_author']
                update_dict['music_title'] = data['music_title']
                update_dict['music_url'] = data['music_url']
                update_dict['origin_cover'] = data['origin_cover']
                update_dict['dynamic_cover'] = data['dynamic_cover']
                update_dict['tag_1'] = data['tag_1']
                update_dict['tag_2'] = data['tag_2']
                update_dict['tag_3'] = data['tag_3']
                update_dict['digg_count'] = data['digg_count']
                update_dict['comment_count'] = data['comment_count']
                update_dict['collect_count'] = data['collect_count']
                update_dict['share_count'] = data['share_count']
                update_dict['extra'] = data['extra']
                update_dict['load_if'] = 0
                update_dict['load_sts'] = 0
                update_dict['del_if'] = 0
                gather_day_data = GatherDay(**update_dict)
                session.merge(gather_day_data)
                session.commit()
        return 'success'
    except Exception as e:
        session.commit()
        session.close()
        return e


def download_video_by_id(uid, video_id):
    url = server_url + 'single/'
    stmt = select(GatherDay).where(GatherDay.uid == uid and GatherDay.video_id == video_id)
    result = session.execute(stmt).fetchone()[0]
    result_json = dict()
    result_json['author'] = result.nickname
    result_json['describe'] = result.desc
    result_json['dynamic'] = result.dynamic_cover
    result_json['music'] = result.music_url
    result_json['origin'] = result.origin_cover
    result_json['preview'] = result.origin_cover
    result_json['text'] = "获取作品数据成功！"
    result_json['url'] = result.share_url
    result_json['download'] = True
    response = requests.request("POST", url, headers=headers, data=json.dumps(result_json))
    response_data = response.json()
    if response.status_code != 200:
        response_data = response.json()
        return response_data
    else:
        return response_data['text']


def update_settings(para: dict):
    url = server_url + 'settings/'
    response = requests.request("POST", url, headers=headers, data=para)
    response_data = response.json()
