from django.db import models


# Create your models here.
class Area(models.Model):

    class Meta:
        verbose_name = "地区前缀"
        verbose_name_plural = "地区前缀"

    prefix = models.CharField('手机前缀', max_length=7)
    area_code = models.CharField('地区区号', max_length=4)
    area_pro = models.CharField('省份',max_length=10,db_column='area_name')
    area_city = models.CharField('城市',max_length=10)
    mobile_carrier = models.CharField('运营商', max_length=8)
