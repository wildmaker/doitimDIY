from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    # 注册
    path('register/', views.register, name = 'register'),
    # 登录
    path('login/', views.login, name = 'login'),
    # 注销
    path('logout/', views.logout, name = 'logout'),
    # 改密码
    path('change-password/', auth_views.PasswordChangeView.as_view())
]