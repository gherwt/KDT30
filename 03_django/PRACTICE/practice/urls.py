from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('util/', include('util.urls')),
    path('school/', include('crud.urls')),
]
