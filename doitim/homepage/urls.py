from django.urls import path, re_path
from . import views

app_name = 'homepage'
urlpatterns = [
    # 主页
    path('', views.index, name = 'index')
]