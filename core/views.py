
from django.http import JsonResponse
import json

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def api(request):
    if request.method == 'POST':
        request_body = request.body
        data = json.loads(request_body.decode('utf-8'))
        my_data = data['RewriteE164Rsp']
        my_data['calleeE164'] = 'xyz'
        return JsonResponse({'RewriteE164Rsp':my_data})
