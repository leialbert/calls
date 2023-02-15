from django.contrib import admin

# Register your models here.
from .models import BlackPhone
@admin.register(BlackPhone)
class BlackPhoneAdmin(admin.ModelAdmin):
    list_display = ['id','level','phone']