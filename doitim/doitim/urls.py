from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('homepage.urls')),
    path('todo/', include('todo.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
    # My test scripts
    # URL reverse using instance namespace in URL config
]