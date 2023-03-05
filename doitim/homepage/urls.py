from django.urls import path, re_path
from django.views.i18n import JavaScriptCatalog
from . import views
urlpatterns = [
    # 主页
    re_path(r'^$', views.index, name = "index"),
]