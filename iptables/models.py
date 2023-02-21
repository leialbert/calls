from django.db import models

# Create your models here.
class IPTable(models.Model):
    class Meta:
        verbose_name = "IP白名单"
        verbose_name_plural = "IP白名单"

    ip_address = models.GenericIPAddressField('IP',protocol='IPv4',unique=True)
    remark = models.CharField('备注',max_length=20)
    created_at = models.DateTimeField('添加时间',auto_now_add=True)
    def __str__(self):
        return f'{self.ip_address} ({self.remark})'

class Rule(models.Model):
    class Meta:
        verbose_name_plural = "规则设置"

    name = models.CharField('规则名称',max_length=20)
    ip = models.ForeignKey(IPTable, verbose_name="IP地址", on_delete=models.CASCADE)
    callee_prefix = models.CharField('被叫前缀',max_length=10)