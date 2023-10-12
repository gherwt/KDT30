from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('crud:index')
    
    # UserCreationForm 을 활용한 회원 가입 
    if request.method == "POST":
        # 양식에 맞으면, 유효하다면 Data 를 form 에서 저장하고 로그인한다
        form = UserCreationForm(data = request.POST)       
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('crud:index')
        
    else:
        form = UserCreationForm()       

    return render(request, 'accounts/signup.html', {
        'form' : form
    })

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('crud:index')
    # AuthenticationForm 을 활용한 로그인
    if request.method == "POST":
        # POST 된 request 를 AuthenticationForm 을 활용해 저장된 데이터와 비교
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('crud:index')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {
        'form' : form
    })

# logout 구현
def logout(request):

    # logout 을 활용함
    auth_logout(request)
    
    return redirect('crud:index')
