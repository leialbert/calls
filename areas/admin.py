from django.contrib import admin

# Register your models here.
from .models import Area
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    search_fields = ['prefix','area_code','area_name','mobile_carrier']
    list_filter = ['area_name']
    list_display = ['prefix','area_code','area_name','mobile_carrier']
    list_per_page = 30