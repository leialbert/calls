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
    list_display = ['name','ip','callee_prefix']
