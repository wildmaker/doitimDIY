from django.urls import path
from . import views

app_name = 'print_current_page_url'
urlpatterns = [
    path('/success', views.index, name = 'index')
]