from django.contrib import admin

# Register your models here.
from .models import Log
@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    search_fields = ['call_type','call_Id','caller','callee']
    list_filter = (
        ('created_at', admin.DateFieldListFilter),
    )
    date_hierarchy = 'created_at'
    list_display = ['call_type','call_Id','caller','callee','created_at']
    list_per_page = 30