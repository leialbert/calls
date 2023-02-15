from logs.models import Log
from areas.models import Area
from django.http import JsonResponse
import json

re_log = Log()
re_area = Area()

def api(request):
    if request.method == 'POST':
        request_body = request.body
        data = json.loads(request_body.decode('utf-8'))
        my_data = data['RewriteE164Rsp']
        re_log.call_Id = my_data['callId']
        re_log.call_type = 'rewrite'
        re_log.caller = my_data['callerE164']
        re_log.callee = my_data['calleeE164']
        re_log.save()
        
        return JsonResponse({'RewriteE164Rsp':my_data})
