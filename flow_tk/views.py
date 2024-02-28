import json
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.views.decorators.http import require_POST
from custom.tk_post import (
    search_data,
    search_data_save,
    search_data_by_account,
    download_video_by_id,
)
import demjson3 as demjson



@require_POST
def getSearchData:



# 上传采集配置文件
@require_POST
def text(request):
    response_data = dict()
    try:
        # 解析JSON数据
        request_data = demjson.decode(request.body)
        # 采集数据结果
        return_data = search_data_save(request_data)
        response_data["data"] = return_data
        return JsonResponse(response_data)
    except Exception as e:
        return HttpResponseBadRequest(e)


# 采集数据
@require_POST
def search(request):
    response_data = dict()
    try:
        request_data = json.loads(request.body)  # 解析JSON数据
        # 采集数据结果
        data = search_data(request_data)
        if data["message"] == "success":
            # 存入数据库
            search_data_save(data)
            response_data["status"] = 200
            response_data["msg"] = "success"
            response_data["data"] = data
            return JsonResponse(response_data)
        else:
            response_data["status"] = 500
            response_data["msg"] = "fail"
            response_data["data"] = data
            return JsonResponse(response_data)
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


@require_POST
def account(request):
    response_data = dict()
    try:
        request_data = json.loads(request.body)  # 解析JSON数据
        # 采集数据结果
        data = search_data_by_account(request_data)
        if data["message"] == "success":
            # 存入数据库
            return_data = search_data_save(data["data"])
            response_data["status"] = 200
            response_data["msg"] = "success"
            response_data["data"] = return_data
            return JsonResponse(response_data)
        else:
            response_data["status"] = 500
            response_data["msg"] = "fail"
            response_data["data"] = data
            return JsonResponse(response_data)
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


# 下载数据
@require_POST
def download_video(request):
    response_data = dict()
    try:
        request_data = json.loads(request.body)  # 解析JSON数据
        # 处理数据...
        if (
            request_data["uid"] is not None
            and request_data["uid"] != ""
            and request_data["video_id"] is not None
            and request_data["video_id"] != ""
        ):
            data = download_video_by_id(request_data["uid"], request_data["video_id"])
            response_data["status"] = 200
            response_data["msg"] = "success"
            response_data["data"] = data
            return JsonResponse(response_data)
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


# todo:修改配置文件
# @require_POST
# def settings(request):
#     try:
#         request_data = json.loads(request.body)  # 解析JSON数据
#         # 处理数据...
#         if request_data['cookie']:
#             data = download_video_by_id(request_data['uid'], request_data['video_id'])
#             response_data['status'] = 200
#             response_data['msg'] = 'success'
#             response_data['data'] = data
#             return JsonResponse(response_data)
#     except json.JSONDecodeError:
#         return HttpResponseBadRequest('Invalid JSON')
