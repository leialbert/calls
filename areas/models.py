from django.db import models


# Create your models here.
class Area(models.Model):

    class Meta:
        verbose_name = "地区前缀"
        verbose_name_plural = "地区前缀"

    prefix = models.CharField('手机前缀', max_length=7)
    area_code = models.CharField('地区区号', max_length=4)
    area_name = models.CharField('地区名称', max_length=10)
    mobile_carrier = models.CharField('运营商', max_length=8)
