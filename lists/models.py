from django.db import models

# Create your models here.

class BlackList(models.Model):
    class Meta:
        verbose_name_plural = '黑名单列表'
    phone = models.CharField('号码',max_length=11)
    created_at = models.DateTimeField('添加时间',auto_now_add=True)
    def __str__(self):
        return f'{self.phone}'