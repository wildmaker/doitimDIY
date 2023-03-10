from django.urls import path
from . import views

urlpatterns = [
    path('json-response', views.json_response, name = 'json-response')
]