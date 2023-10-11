from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout


# 계정 생성 -> 권한을 부여한다.
@require_http_methods(['GET', 'POST'])
def signup(request):
    # 요청 보낸 사용자가 인증되었다면 => 바로 돌려보내기
    if request.user.is_authenticated:
        return redirect('board:index')
    if request.method == 'POST':
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            # 회원 가입 후 정보를 저장해준다. 
            user = form.save()
            auth_login(request, user)
            return redirect('board:index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html',{
        'form' : form,
    })

@require_http_methods(['GET', 'POST'])
def login(request):
    # 요청 보낸 사용자가 인증되었다면 => 바로 돌려보내기
    if request.user.is_authenticated:
        return redirect('board:index')
    if request.method == 'POST':
        # id, password 검증해주는 것
        # 사용자 특정짓기
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            # 쿠키(팔찌) 세팅
            auth_login(request, user)
            return redirect('board:index')
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html',{
        'form' : form,
    })


def logout(request):
    auth_logout(request)
    return redirect('board:index')