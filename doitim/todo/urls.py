from django.urls import path, re_path
from . import views

urlpatterns = [
    # 主页
    re_path(r'^$', views.index, name = "index"),

    # # 显示所有主题
    re_path(r'^home/$', views.home, name = "home"),
    # # 显示所有主题
    re_path(r'^items/$', views.items, name = "items"),
    # # 显示所有主题
    re_path(r'^today/$', views.today, name = "today"),

    # # 特定主题的详细页面
    # re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name = 'topic'),

    # # 用于添加新主题的网页
    re_path(r'^new_item/$', views.new_item, name = 'new_item'),

    # 用于添加新条目的页面
    # re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name = 'new_entry'),

    # # 用于编辑现有条目
    # re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name = 'edit_entry')
]