from django.db import models

# Create your models here.
class BlackPhone(models.Model):
    class Meta:
        verbose_name = "黑名单号码"
        verbose_name_plural = "黑名单号码"


    levels = (
        (0,'12321'),
        (1,'自定义组1'),
        (2,'自定义组2')
    )
    level = models.IntegerField('级别',choices=levels)
    phone = models.CharField('号码',max_length=11)

class WhitePhone(models.Model):
    class Meta:
        verbose_name = "白名单号码"
        verbose_name_plural = "白名单号码"


    levels = (
        (0,'自定义组1'),
        (1,'自定义组2'),
        (2,'自定义组3')
    )
    level = models.IntegerField('级别',choices=levels)
    phone = models.CharField('号码',max_length=11)