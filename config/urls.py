from django.contrib import admin
from django.urls import path

admin.site.site_header = "Django REST framework Docker Administration"
admin.site.index_title = "Administration"
admin.site.site_title = "DRF Docker"

urlpatterns = [
    path('admin/', admin.site.urls),
]
