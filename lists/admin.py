from django.contrib import admin

# Register your models here.
from .models import BlackPhone,WhitePhone
@admin.register(BlackPhone)
class BlackPhoneAdmin(admin.ModelAdmin):
    list_filter = ['level']
    search_fields = ['phone']
    list_display = ['id','level','phone']

@admin.register(WhitePhone)
class WhitePhoneAdmin(admin.ModelAdmin):
    list_filter = ['level']
    search_fields = ['phone']
    list_display = ['id','level','phone']