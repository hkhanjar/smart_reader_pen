
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from smartAPI.views import api_reader


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/v1/reader/$', api_reader, name='ocr'),
]
