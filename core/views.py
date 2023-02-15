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
    # else:
    #     allprefix = Area.objects.all()
    #     for obj in allprefix:
    #         obj.area_city = obj.area_pro.split('-')[-1]
    #         obj.area_pro = obj.area_pro.split('-')[0]
    #         print('I am update the area %s' %obj.area_pro)
    #         obj.save()
