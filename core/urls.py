from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/rewrite/',views.api, name='api'),
    path("admin/", admin.site.urls),
]
