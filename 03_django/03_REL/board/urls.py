from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('',views.index, name = 'index'),
    # path('new/',views.new, name = 'new'),
    path('create/',views.create, name = 'create'),
    path('<int:pk>/',views.detail, name = 'detail'),
    path('<int:pk>/edit/',views.edit, name = 'edit'),
    # path('<int:pk>/update/',views.update, name = 'update'),
    path('<int:pk>/delete/',views.delete, name = 'delete'),

    # board/1/comments/create/
    path('<int:pk>/comments/create/', views.create_comment, name ='create_comment'),
    # board/1/comments/1/delete/
    path('<int:pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name ='delete_comment'),
    # borad/1/like/
    path('<int:pk>/like/', views.like, name = 'like'),
]

