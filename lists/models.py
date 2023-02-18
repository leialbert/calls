from django.db import models

# Create your models here.

class Level(models.Model):
    class Meta:
        verbose_name_plural = "自定义组"
    grp_tpe = [
        ('黑名单','黑名单'),
        ('白名单','白名单'),
    ]
    group_type = models.CharField('群组类型',choices=grp_tpe,max_length=8)
    level = models.CharField('自定义组名',max_length=12)
    created_at = models.DateTimeField('添加时间',auto_now_add=True)
    def __str__(self):
        return f'{self.group_type} -- ({self.level})'
    
class Phone(models.Model):
    class Meta:
        verbose_name = "电话号码"
        verbose_name_plural = "电话号码"

    level = models.ForeignKey(Level,on_delete=models.CASCADE)
    phone = models.CharField('号码',max_length=11)
    created_at = models.DateTimeField('添加时间',auto_now_add=True)

# class BlackPhone(models.Model):
#     class Meta:
#         verbose_name = "黑名单号码"
#         verbose_name_plural = "黑名单号码"

#     level = models.ForeignKey(Level,on_delete=models.CASCADE)
#     phone = models.CharField('号码',max_length=11)
#     created_at = models.DateTimeField('添加时间',auto_now_add=True)
    

# class WhitePhone(models.Model):
#     class Meta:
#         verbose_name = "白名单号码"
#         verbose_name_plural = "白名单号码"

#     level = models.ForeignKey(Level,on_delete=models.CASCADE)
#     phone = models.CharField('号码',max_length=11)
#     created_at = models.DateTimeField('添加时间',auto_now_add=True)
#     def __str__(self):
#         return f'{self.level}'