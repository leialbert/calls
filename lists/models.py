from django.db import models

# Create your models here.
class BlackPhone(models.Model):
    class Meta:
        verbose_name = "Black Phone"
        verbose_name_plural = "Black Phones"


    levels = (
        (0,'12321'),
        (1,'自定义组1'),
        (2,'自定义组2')
    )
    level = models.IntegerField('级别',choices=levels)
    phone = models.CharField('号码',max_length=11)