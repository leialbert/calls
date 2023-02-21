from logs.models import Log
from areas.models import Area
from iptables.models import IPTable
from django.http import JsonResponse
import json
from django.core.exceptions import PermissionDenied

# IP 白名单过滤
def require_specific_ips(view_func):
    def wrapper(request, *args, **kwargs):
        allowed_ips = IPTable.objects.all().values_list('ip_address',flat=True)      
        if request.method == 'POST' and request.META.get('REMOTE_ADDR') not in allowed_ips:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper

re_log = Log()
re_area = Area()
@require_specific_ips
def rewrite(request):
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
@require_specific_ips
def vosblack(request):
    # def check():
    # post_param = request.get_data().decode()
    # jsonrequest = json.loads(post_param)    
    # real_callee = jsonrequest['callee'][-11:]
    # if(collection.find_one({'phone':real_callee})):
    #     callId = jsonrequest['callId']
    #     res_str = '{"callId":%d,"forbid":1,"transactionId":"910821-128385"}'%callId
    #     db.logs.insert_one({'callTime':datetime.datetime.now(),'callee':real_callee, 'type':1})
    #     return res_str
    # else:
    #     callId = jsonrequest['callId']
    #     res_str ='{"callId":%d}'%callId
    #     return res_str
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