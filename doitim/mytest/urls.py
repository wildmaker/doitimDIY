from django.urls import path
from . import views

app_name = 'mytest'

urlpatterns = [
    path('json-response/', views.json_response, name = 'json-response'),
    path('bootstrap/',views.bootstrap,name='bootstrap')

]