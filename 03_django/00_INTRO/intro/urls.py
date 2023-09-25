"""
URL configuration for intro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from first_app import views


# request -> response -> view 가 한 circle 임.
# 이것을 얼마나 확장시킬 수 있는가????

urlpatterns = [
    path('admin/', admin.site.urls),

    # 주석 처리 시 읽지 못해 응답 불가능 메시지가 뜬다. 해석할 수 없다.
    path('hello/', views.hello),
    # url hello/ 로 요청이 들어오면, ~~~~ 일을 한다. 함수가 들어와야 한다.
    path('bye/', views.bye),
    # URL pattern 'lotto/' -> 화면에 로또번호 6개를 뽑아서 줌
    path('lotto/', views.lotto),
    path('lunch/', views.lunch),
]


# request -> (http://127.0.0.1:8000/) hello/
# Response -> 'hello django'
