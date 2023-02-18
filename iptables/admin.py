from django.contrib import admin

# Register your models here.
from .models import IPTable,Rule

@admin.register(IPTable)
class IPTableAdmin(admin.ModelAdmin):
    search_fields = ['ip_address','remark','created_at']
    list_display = ['ip_address','remark','created_at']

@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    search_fields = ['callee_prefix']
    list_filter = ['phone_group']
    list_display = ['name','ip','priority','phone_group_level','callee_prefix']
    def phone_group_level(self,obj):
        return obj.phone_group.level