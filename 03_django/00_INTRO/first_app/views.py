from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

# 1. function view
# 2. class view
# 이곳으로 url 파일을 가져오면 url 로는 사용할 수 없다..


def hello(request):
    return render(request, 'hello.html')

def bye(request):
    return render(request, 'bye.html')

def lotto(request):
    lucky_numbers = random.sample(range(1, 46), 6)
    lucky_numbers.sort()
    context = {
        'message' : '부자되고 싶다!!',
        'lucky_numbers' : lucky_numbers,
    }
    
    return render(request, 'lotto.html', context)

def lunch(request):
    menus = ['중식', '양식', '일식', '한식', '패스트푸드', '편의점']
    lunch_menu = random.choice(menus)
    
    context = {
        'message' : '오늘의 점심은????',
        'lunch_menu': lunch_menu,
    }
    return render(request, 'lunch.html', context)
