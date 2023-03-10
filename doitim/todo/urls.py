from django.urls import path, re_path
from . import views, my_test
from django.views.i18n import JavaScriptCatalog

app_name = 'todo'

urlpatterns = [
    # accept null slug
    path('', views.index, name='index-default'),

    # item_form
    path('item_form/', views.item_form, name="item_form"),
    # today
    path('<slug:slug>/', views.index, name='index'),

    path('jsi18n/', JavaScriptCatalog.as_view(), name='js_catlog'),

    # today_v2
    re_path(r'^today/$', views.today_v2, name="today_v2"),

    # # 用于添加新主题的网页
    re_path(r'^new_item/$', views.new_item, name='new_item'),

    path('test', my_test.test, name="test"),
    path('test2', my_test.test2, name="test2")

]
