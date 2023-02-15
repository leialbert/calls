from django.contrib import admin
from django.utils import timezone

# Register your models here.
from .models import BlackPhone,WhitePhone
@admin.register(BlackPhone)
class BlackPhoneAdmin(admin.ModelAdmin):
    list_filter = ['level']
    search_fields = ['phone']
    list_display = ['id','level','phone','created_at_formatted']
    def created_at_formatted(self,obj):
        return timezone.localtime(obj.created_at).strftime('%Y-%m-%d %H:%M:%S')
    created_at_formatted.short_description = '创建时间'

@admin.register(WhitePhone)
class WhitePhoneAdmin(admin.ModelAdmin):
    list_filter = ['level']
    search_fields = ['phone']
    list_display = ['id','level','phone','created_at_formatted']
    def created_at_formatted(self,obj):
        return timezone.localtime(obj.created_at).strftime('%Y-%m-%d %H:%M:%S')
    created_at_formatted.short_description = '创建时间'