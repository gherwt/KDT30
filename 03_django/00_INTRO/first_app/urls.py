from django.urls import path
from . import views

urlpatterns = [

     # 주석 처리 시 읽지 못해 응답 불가능 메시지가 뜬다. 해석할 수 없다.
    path('hello/', views.hello),
    # url hello/ 로 요청이 들어오면, ~~~~ 일을 한다. 함수가 들어와야 한다.
    path('bye/', views.bye),
    # URL pattern 'lotto/' -> 화면에 로또번호 6개를 뽑아서 줌
    path('lotto/', views.lotto),
    # lunch/
    path('lunch/', views.lunch),

]
