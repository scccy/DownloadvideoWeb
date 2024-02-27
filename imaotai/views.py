from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from DownloadvideoWeb import settings
from custom.mt_post import (
    init_headers, get_location, get_vcode, login, select_geo
)
import json


# Create your views here.


# 发送验证码 手机号码是字符串
@require_POST
def get_mobile(request):
    init_headers()
    response_data = dict()
    mobile = json.loads(request.body)['mobile']
    try:
        get_vcode(mobile)
        response_data['msg'] = '验证码发送成功'
        response_data['status'] = '200'
        return JsonResponse(response_data)
    except Exception as e:
        response_data['msg'] = e
        response_data['status'] = '500'
        return JsonResponse(response_data)


# 确认附近位置，返回高德搜索列表
@require_POST
def get_loaction(request):
    response_data = dict()
    request_data = json.loads(request.body)
    city = request_data['city']
    province = request_data['province']
    address = request_data['address']
    amap_key = settings.AMAP_KEY
    location_select = select_geo(province=province, city=city, amap_key=amap_key, address=address)
    # location: str = location_select["location"]
    response_data['msg'] = '验证码发送成功'
    response_data['status'] = '200'
    response_data['data'] = location_select
    return JsonResponse(response_data)
# todo:收到确认的地址存入配置文件
# @require_POST
# def get_location_sure(request):


# def get_imaotai(request):
#     request_data = json.loads(request.body)
#     items = []
#
#     init_headers()
#     location_select: dict = get_location()
#     province = location_select["province"]
#     city = location_select["city"]
#     location: str = location_select["location"]
#
#     mobile = input("输入手机号[18888888888]:").strip()
#     get_vcode(mobile)
#     code = input(f"输入 [{mobile}] 验证码[8888]:").strip()
#     token, user_id = login(mobile, code)
#     item = {
#         "city": str(city),
#         "lat": location.split(",")[1],
#         "lng": location.split(",")[0],
#         "mobile": str(mobile),
#         "province": province,
#         "token": str(token),
#         "userid": str(userId),
#         "reserve_rule": 0,
#         "item_codes": ["10941", "10942"],
#     }
#     items.append(item)
#     condition = input("是否继续添加账号[y/n]:").strip()
#     with open("account.json", "w") as f:
#         f.write(json.dumps(items, ensure_ascii=False, indent=4))
#     if condition.lower() == "n":
#        pass
