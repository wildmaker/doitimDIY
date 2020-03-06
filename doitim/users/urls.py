from django.urls import path, re_path
from . import views

urlpatterns = [
    # 登录
    re_path(r'^login/$', views.userlogin, name = 'userlogin'),
    # 注销
    re_path(r'^logout/$', views.userlogout, name = 'logout'),
    # 注册
    re_path(r'^register/$', views.register, name = 'register')
]