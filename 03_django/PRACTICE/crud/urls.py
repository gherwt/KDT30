from django.urls import path
from . import views


# <app_name>:<pattern_name>
# URL 을 변수로 사용하기 => app_name : name
# pattern name 을 설정해주면 자동으로 url이 할당된다.

app_name = 'crud'


urlpatterns = [
    path('', views.index, name = 'index'), # ex) crud:index
    path('new/', views.new, name = 'new'), # ex) crud:new
    path('<int:pk>/', views.detail, name = 'detail'), # ex) crud:detail
    path('<int:pk>/update/', views.update, name = 'update'), # ex) crud:edit
    path('<int:pk>/delete/', views.delete, name = 'delete'),  # ex) crud:delete
    
    # comment creat, delete url 설정해주기
    path('<int:pk>/univ/create/', views.reply_create, name = 'reply_create'), 
    path('<int:pk>/univ/<int:reply_pk>/delete/', views.reply_delete, name = 'reply_delete'),  

]
