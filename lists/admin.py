from django.contrib import admin
from django.utils import timezone

# Register your models here.
from .models import BlackList
@admin.register(BlackList)
class BlackListAdmin(admin.ModelAdmin):
    list_display = ['phone','created_at_formatted']
    def created_at_formatted(self,obj):
        return timezone.localtime(obj.created_at).strftime('%Y-%m-%d %H:%M:%S')
    created_at_formatted.short_description = '创建时间'
