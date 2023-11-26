from django.urls import path, re_path
from . import views, tests
from django.views.i18n import JavaScriptCatalog

app_name = 'todo'

urlpatterns = [
    path('all/', views.all, name='all'),
    path('today/', views.today, name='today'),
    path('tomorrow/', views.tomorrow, name='tomorrow'),
    path('next_7_days/', views.next_7_days, name='next_7_days'),
    path('test/',tests.send_post, name = 'test'),
    # 用于添加新主题的网页
    re_path(r'^new/$', views.new, name='new'),
    re_path(r'^update/$', views.update, name='update'),
    # accept null slug
    path('', views.index, name='index-default'),
    # i18n
    path('jsi18n/', JavaScriptCatalog.as_view(), name='js_catlog'),

    # today_v2
    re_path(r'^today/$', views.today_v2, name="today_v2")
]
