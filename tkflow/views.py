import json
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.views.decorators.http import require_POST
from custom.post_gather_view import search_data

response_data = {
    'status': int(),
    'msg': '',
    'data': ''

}

# 将字典转换为JSON字符串
json_data = json.dumps(response_data)


@require_POST
def search(request):
    try:
        request_data = json.loads(request.body)  # 解析JSON数据
        # 处理数据...
        data = search_data(request_data)
        response_data['status'] = 200
        response_data['msg'] = 'success'
        response_data['data'] = data
        return JsonResponse(response_data)
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid JSON')
