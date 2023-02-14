from django.db import models

# Create your models here.
class Log(models.Model):

    class Meta:
        verbose_name = "Log"
        verbose_name_plural = "Logs"

    # {"RewriteE164Req":{"callId":123137,"callerE164":"020cuishou","calleeE164":"3313941135255"}}
    call_type = models.CharField('请求类型',max_length=8)
    call_Id = models.IntegerField('呼叫ID')
    caller = models.CharField('主叫号码',max_length=20)
    callee = models.CharField('被叫号码',max_length=20)
    created_at = models.DateTimeField('请求时间',auto_now_add=True)