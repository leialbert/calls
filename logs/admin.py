from django.contrib import admin
from django.utils import timezone


# Register your models here.
from .models import Log
@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    search_fields = ['call_type','call_Id','caller','callee']
    list_filter = (
        ('created_at', admin.DateFieldListFilter),
    )
    # '%Y-%m-%d %H:%M:%S.%f'
    date_hierarchy = 'created_at'

    list_display = ['call_type','call_Id','caller','callee','created_at_formatted']
    def created_at_formatted(self,obj):
        return timezone.localtime(obj.created_at).strftime('%Y-%m-%d %H:%M:%S.%f')
    created_at_formatted.short_description = 'Created at'

    list_per_page = 30