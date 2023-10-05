from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new),
    path(' ', views.index),
    path('create/', views.create),
    path('<int:pk>/', views.detail),
    path('edit/', views.edit),
    path('update/', views.update),
    path('delete/', views.delete),
]

