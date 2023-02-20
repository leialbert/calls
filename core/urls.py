from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('api/v1/rewrite/',views.rewrite, name='rewrite'),
    path('api/v1/vosblack/',views.vosblack,name='vosblack'),
    path("admin/", admin.site.urls),
    path('logs/',include('logs.urls')),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
