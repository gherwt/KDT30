from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout


# 계정 생성 -> 권한을 부여한다.
@require_http_methods(['GET', 'POST'])
def signup(request):
    print(request.user)
    if request.method == 'POST':
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('board:index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html',{
        'form' : form,
    })
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        # id, password 검증해주는 것
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