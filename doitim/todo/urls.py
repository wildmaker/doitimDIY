from django.urls import path, re_path
from . import views, my_test
from django.views.i18n import JavaScriptCatalog

app_name = 'todo'

urlpatterns = [
    path('all/', views.all, name='all'),
    path('today/', views.today, name='today'),
    path('tomorrow/', views.tomorrow, name='tomorrow'),
    path('next_7_days/', views.next_7_days, name='next_7_days'),
    # 用于添加新主题的网页
    re_path(r'^new/$', views.add_or_update_todo, name='new'),
    re_path(r'^update/$', views.add_or_update_todo, name='update'),
    # accept null slug
    path('', views.index, name='index-default'),
    # i18n
    path('jsi18n/', JavaScriptCatalog.as_view(), name='js_catlog'),

    # today_v2
    re_path(r'^today/$', views.today_v2, name="today_v2"),

    # # 用于添加新主题的网页

    path('test/', my_test.test, name="test"),
    path('test2/', my_test.test2, name="test2")

]
