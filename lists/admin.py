from django.contrib import admin
from django.utils import timezone

# Register your models here.
from .models import Level,Phone


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ['group_type','level','created_at_formatted']
    def created_at_formatted(self,obj):
        return timezone.localtime(obj.created_at).strftime('%Y-%m-%d %H:%M:%S')
    created_at_formatted.short_description = '创建时间'

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_filter = ['level']
    search_fields = ['phone']
    list_display = ['level','phone','created_at_formatted']
    def created_at_formatted(self,obj):
        return timezone.localtime(obj.created_at).strftime('%Y-%m-%d %H:%M:%S')
    created_at_formatted.short_description = '创建时间'


# @admin.register(WhitePhone)
# class WhitePhoneAdmin(admin.ModelAdmin):
#     list_filter = ['level']
#     search_fields = ['phone']
#     list_display = ['id','level','phone','created_at_formatted']
#     def created_at_formatted(self,obj):
#         return timezone.localtime(obj.created_at).strftime('%Y-%m-%d %H:%M:%S')
#     created_at_formatted.short_description = '创建时间'
