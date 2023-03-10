from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('homepage.urls')),
    path('todo/', include('todo.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
    # My test scripts
    path('test/', include('mytest.urls')),
    # URL reverse using instance namespace in URL config
    path('customer/pay/',include('print_current_page_url.urls', namespace = 'print_current_page_url-customer')),
    path('employee/pay/',include('print_current_page_url.urls', namespace = 'print_current_page_url-employee'))
]