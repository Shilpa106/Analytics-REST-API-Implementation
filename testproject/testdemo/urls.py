"""testdemo URL Configuration
"""
from django.contrib import admin
from django.urls import path,include
from fliter_api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/upload/',UploadFileView.as_view(),name='upload'),
    path('api/get/',GetData.as_view(),name='get')
]