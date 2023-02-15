from django.contrib import admin

# Register your models here.
from .models import Area
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    search_fields = ['prefix','area_code','area_pro','area_city','mobile_carrier']
    list_filter = ['area_pro']
    list_display = ['prefix','area_code','area_pro','area_city','mobile_carrier']
    list_per_page = 30