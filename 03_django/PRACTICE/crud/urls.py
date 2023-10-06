from django.urls import path
from . import views


# URL 을 변수로 사용하기 => app_name : name

app_name = 'crud'

urlpatterns = [
    path('', views.index, name = 'index'), # ex) crud:new
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name = 'create'),
    path('<int:pk>/', views.detail, name = 'detail'),
    path('<int:pk>/edit/', views.edit, name = 'edit'),
    path('<int:pk>/update/', views.update, name = 'update'),
    path('<int:pk>/delete/', views.delete, name = 'delete'),  
]
