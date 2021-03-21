
from django.contrib import admin
from django.urls import path
from main.views import index
# main폴더에 views.py파일에 index함수와 연결 -> 기본 yrl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
]
